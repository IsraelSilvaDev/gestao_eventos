from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from .models import Evento
from .forms import CodigoAcessoForm, RespostaForm

# --- Views Públicas (para Convidados) ---

def home_view(request):
    """Página inicial pública para inserir o código do evento."""
    if request.method == 'POST':
        
        form = CodigoAcessoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            try:
                evento = Evento.objects.get(codigo_acesso=codigo)
                # Redireciona para o formulário de resposta desse evento
                return redirect('responder_evento', codigo_acesso=evento.codigo_acesso)
            except Evento.DoesNotExist:
                messages.error(request, 'Código de acesso inválido. Tente novamente.')
    else:
        form = CodigoAcessoForm()
    
    return render(request, 'home.html', {'form': form})

def responder_evento_view(request, codigo_acesso):
    """Página do formulário de RSVP para um evento específico."""
    evento = get_object_or_404(Evento, codigo_acesso=codigo_acesso)
    
    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            response = form.save(False)
            response.evento = evento
            response.save()
            # Redireciona para a página de sucesso
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
    
    # Garante que o usuário só possa ver eventos que ele criou
    evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
    
    # Busca todas as respostas do evento
    respostas = evento.respostas.all().order_by('-data_resposta')
    
    # --- Cálculos do Resumo ---
    
    # Total de Pessoas Confirmadas (Soma do campo 'total_pessoas' de quem confirmou)
    soma_pessoas_confirmadas = respostas.filter(status='confirmado').aggregate(
        total=Coalesce(Sum('total_pessoas'), 0)
    )['total']
    
    # Total de Respostas "Confirmado"
    total_confirmados = respostas.filter(status='confirmado').count()
    
    # Total de Respostas "Declinado"
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