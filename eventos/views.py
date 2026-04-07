from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from .models import Evento, Convite, Resposta
from .forms import CodigoAcessoForm, RespostaForm, EventoForm
#
# --- Views Públicas (para Convidados) ---

def home_view(request):
    """Página inicial pública para inserir o código do evento."""
    if request.method == 'POST':

        form = CodigoAcessoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            try:
                convite = Convite.objects.get(codigo_acesso=codigo)
                return redirect('responder_evento', codigo_acesso=convite.codigo_acesso)
            except Convite.DoesNotExist:
                messages.error(request, 'Código de acesso inválido. Tente novamente.')
    else:
        form = CodigoAcessoForm()

    return render(request, 'home.html', {'form': form})

def responder_evento_view(request, codigo_acesso):
    """Página do formulário de RSVP para um evento específico."""
    convite = get_object_or_404(Convite, codigo_acesso=codigo_acesso)
    evento = convite.evento

    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            response = form.save(False)
            response.convite = convite
            response.save()
            return redirect('sucesso')
    else:
        form = RespostaForm()

    context = {
        'form': form,
        'evento': evento
    }
    return render(request, 'responder_evento.html', context)

def sucesso_view(request):
    """Página de "Obrigado por responder"."""
    return render(request, 'sucesso.html')


# --- Views do Organizador (Área Restrita) ---

def is_organizador(user):
    """Verifica se o usuário é um 'staff', que consideramos um organizador."""
    return user.is_authenticated and user.is_staff

@login_required(login_url='login')
@user_passes_test(is_organizador)
def dashboard_view(request):
    """Página principal do dashboard do organizador."""
    # Lista apenas os eventos criados pelo usuário logado
    eventos = Evento.objects.filter(organizador=request.user).order_by('-data')
    return render(request, 'dashboard/dashboard.html', {'eventos': eventos})

@login_required(login_url='login')
@user_passes_test(is_organizador)
def detalhe_evento_dashboard_view(request, evento_id):
    """Página de detalhes do evento, com a lista de respostas e resumo."""

    evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)

    convites = evento.convites.all()
    respostas = Resposta.objects.filter(convite__in=convites).order_by('-data_resposta')

    soma_pessoas_confirmadas = respostas.filter(status='confirmado').aggregate(
        total=Coalesce(Sum('total_pessoas'), 0)
    )['total']

    total_confirmados = respostas.filter(status='confirmado').count()
    total_declinados = respostas.filter(status='declinado').count()

    resumo = {
        'soma_pessoas_confirmadas': soma_pessoas_confirmadas,
        'total_confirmados': total_confirmados,
        'total_declinados': total_declinados,
    }

    context = {
        'evento': evento,
        'respostas': respostas,
        'resumo': resumo
    }
    return render(request, 'dashboard/detalhe_evento.html', context)
@login_required(login_url='login')
@user_passes_test(is_organizador)
def criar_evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)

        if form.is_valid():
            evento = form.save(commit=False)

            evento.organizador = request.user

            evento.save()
            messages.success(request, f'evento "{evento.nome}" foi criado com sucesso!')
            return redirect('dashboard')

    else:
        form = EventoForm()

        context = {
            'form': form,
            'titulo_pagina':'Criar Novo Evento'
        }
        return render(request, 'dashboard/form_evento.html', context)

@login_required(login_url='login')
@user_passes_test(is_organizador)
def editar_evento_view(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, f'O evento "{evento.nome}" foi atualizado com sucesso!')
            return redirect('detalhe_evento', evento_id=evento.id)
    else:
        form = EventoForm(instance=evento)
    context = {
        'form': form,
    }

    return render(request, 'dashboard/form_evento.html', context)
