from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from .models import Evento, Convite, Resposta, Acompanhante
from .forms import CodigoAcessoForm, RespostaForm, EventoForm, ConviteForm, ConviteMultiploForm
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
        if 'desmarcar' in request.POST:
            if hasattr(convite, 'resposta'):
                resposta = convite.resposta
                resposta.acompanhantes.all().delete()
                resposta.delete()
                messages.success(request, 'Sua confirmação foi desmarcada. Você pode confirmar novamente quando desejar.')
            return redirect('responder_evento', codigo_acesso=codigo_acesso)
        
        if hasattr(convite, 'resposta'):
            resposta = convite.resposta
            form = RespostaForm(request.POST, instance=resposta)
            if form.is_valid():
                response = form.save()
                response.acompanhantes.all().delete()
                
                nomes = request.POST.getlist('acompanhante_nome[]')
                documentos = request.POST.getlist('acompanhante_doc[]')
                for nome, doc in zip(nomes, documentos):
                    if nome.strip():
                        Acompanhante.objects.create(
                            resposta=response,
                            nome_completo=nome,
                            documento=doc
                        )
                messages.success(request, 'Sua resposta foi atualizada com sucesso!')
                return redirect('sucesso')
        else:
            form = RespostaForm(request.POST)
            if form.is_valid():
                response = form.save(False)
                response.convite = convite
                response.save()
                
                nomes = request.POST.getlist('acompanhante_nome[]')
                documentos = request.POST.getlist('acompanhante_doc[]')
                for nome, doc in zip(nomes, documentos):
                    if nome.strip():
                        Acompanhante.objects.create(
                            resposta=response,
                            nome_completo=nome,
                            documento=doc
                        )
                return redirect('sucesso')
    else:
        if hasattr(convite, 'resposta'):
            resposta = convite.resposta
            form = RespostaForm(instance=resposta)
            acompanhantes = resposta.acompanhantes.all()
            ja_respondeu = True
        else:
            form = RespostaForm()
            acompanhantes = []
            ja_respondeu = False

    context = {
        'form': form,
        'evento': evento,
        'acompanhantes': acompanhantes,
        'ja_respondeu': ja_respondeu
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
    eventos = Evento.objects.filter(organizador=request.user).order_by('-data')
    convites_do_organizador = Convite.objects.filter(evento__organizador=request.user)
    
    total_convites = convites_do_organizador.count()
    convites_respondidos = convites_do_organizador.filter(resposta__isnull=False).count()
    convites_pendentes = convites_do_organizador.filter(resposta__isnull=True).count()
    
    confirmados = Resposta.objects.filter(convite__evento__organizador=request.user, status='confirmado').count()
    declinados = Resposta.objects.filter(convite__evento__organizador=request.user, status='declinado').count()
    
    taxa_resposta = 0
    if total_convites > 0:
        taxa_resposta = round((convites_respondidos / total_convites) * 100, 1)
    
    eventos_lista = []
    for evento in eventos:
        convites = evento.convites.all()
        confirmados_evento = convites.filter(resposta__status='confirmado').count()
        declinados_evento = convites.filter(resposta__status='declinado').count()
        eventos_lista.append({
            'id': evento.id,
            'nome': evento.nome,
            'data': evento.data,
            'total_convites': convites.count(),
            'confirmados': confirmados_evento,
            'declinados': declinados_evento,
            'codigo': convites.first().codigo_acesso if convites.exists() else ''
        })
    
    context = {
        'eventos': eventos_lista,
        'total_convites': total_convites,
        'convites_respondidos': convites_respondidos,
        'convites_pendentes': convites_pendentes,
        'confirmados': confirmados,
        'declinados': declinados,
        'taxa_resposta': taxa_resposta,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
@user_passes_test(is_organizador)
def estatisticas_dashboard_view(request):
    """Painel de estatísticas de convites."""
    convites_do_organizador = Convite.objects.filter(evento__organizador=request.user)
    total_convites = convites_do_organizador.count()
    convites_respondidos = convites_do_organizador.filter(resposta__isnull=False).count()
    convites_pendentes = convites_do_organizador.filter(resposta__isnull=True).count()
    
    confirmados = Resposta.objects.filter(convite__evento__organizador=request.user, status='confirmado').count()
    declinados = Resposta.objects.filter(convite__evento__organizador=request.user, status='declinado').count()

    eventos = Evento.objects.filter(organizador=request.user)
    eventos_com_estatisticas = []
    for evento in eventos:
        total = evento.convites.count()
        respondidos = evento.convites.filter(resposta__isnull=False).count()
        confirmados_evento = evento.convites.filter(resposta__status='confirmado').count()
        declinados_evento = evento.convites.filter(resposta__status='declinado').count()
        eventos_com_estatisticas.append({
            'nome': evento.nome,
            'total_convites': total,
            'convites_respondidos': respondidos,
            'convites_pendentes': total - respondidos,
            'total_confirmados': confirmados_evento,
            'total_declinados': declinados_evento,
        })

    context = {
        'total_convites': total_convites,
        'convites_respondidos': convites_respondidos,
        'convites_pendentes': convites_pendentes,
        'confirmados': confirmados,
        'declinados': declinados,
        'eventos': eventos_com_estatisticas,
    }
    return render(request, 'dashboard/estatisticas.html', context)

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

    convites_pendentes = convites.filter(resposta__isnull=True).count()

    context = {
        'evento': evento,
        'respostas': respostas,
        'resumo': resumo,
        'convites_pendentes': convites_pendentes
    }
    return render(request, 'dashboard/detalhe_evento.html', context)
@login_required(login_url='login')
@user_passes_test(is_organizador)
def criar_evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)

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
        form = EventoForm(request.POST, request.FILES, instance=evento)
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

@login_required(login_url='login')
@user_passes_test(is_organizador)
def gerenciar_convites_view(request, evento_id):
    """Página para gerenciar convites de um evento."""
    evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
    convites = evento.convites.all()
    convites_pendentes = convites.filter(resposta__isnull=True).count()
    convites_respondidos = convites.filter(resposta__isnull=False).count()
    confirmados_count = convites.filter(resposta__status='confirmado').count()
    declinados_count = convites.filter(resposta__status='declinado').count()
    
    if request.method == 'POST':
        form = ConviteForm(request.POST)
        if form.is_valid():
            convite = form.save(commit=False)
            convite.evento = evento
            convite.save()
            messages.success(request, 'Convite criado com sucesso!')
            return redirect('gerenciar_convites', evento_id=evento.id)
    else:
        form = ConviteForm()
    
    context = {
        'evento': evento,
        'convites': convites,
        'convites_pendentes': convites_pendentes,
        'convites_respondidos': convites_respondidos,
        'confirmados_count': confirmados_count,
        'declinados_count': declinados_count,
        'form': form,
    }
    return render(request, 'dashboard/gerenciar_convites.html', context)

@login_required(login_url='login')
@user_passes_test(is_organizador)
def criar_convites_multiplos_view(request, evento_id):
    """Criar múltiplos convites de uma vez."""
    evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
    
    if request.method == 'POST':
        form = ConviteMultiploForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            nome_base = form.cleaned_data['nome_base'] or 'Convite'
            
            convites_criados = []
            for i in range(quantidade):
                nome_dest = f"{nome_base} {i+1}" if quantidade > 1 else nome_base
                convite = Convite.objects.create(
                    evento=evento,
                    nome_destinatario=nome_dest
                )
                convites_criados.append(convite)
            
            messages.success(request, f'{quantidade} convites criados com sucesso!')
            return redirect('gerenciar_convites', evento_id=evento.id)
    else:
        form = ConviteMultiploForm()
    
    context = {
        'evento': evento,
        'form': form,
    }
    return render(request, 'dashboard/criar_convites_multiplos.html', context)

@login_required(login_url='login')
@user_passes_test(is_organizador)
def excluir_convite_view(request, convite_id):
    """Excluir um convite."""
    convite = get_object_or_404(Convite, id=convite_id, evento__organizador=request.user)
    evento_id = convite.evento.id
    convite.delete()
    messages.success(request, 'Convite excluído com sucesso!')
    return redirect('gerenciar_convites', evento_id=evento_id)

@login_required(login_url='login')
@user_passes_test(is_organizador)
def gerar_link_convite_view(request, convite_id):
    """Gerar link de convite para copiar."""
    convite = get_object_or_404(Convite, id=convite_id, evento__organizador=request.user)
    return JsonResponse({'link': request.build_absolute_uri(f'/evento/{convite.codigo_acesso}/')})


import os
from django.conf import settings as django_settings
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def debug_storage_view(request):
    from django.core.files.storage import default_storage
    import sys
    return JsonResponse({
        'default_storage': str(default_storage.__class__),
        'has_S3_ACCESS_KEY_env': 'S3_ACCESS_KEY' in os.environ,
        'has_S3_SECRET_KEY_env': 'S3_SECRET_KEY' in os.environ,
        'DEFAULT_FILE_STORAGE': getattr(django_settings, 'DEFAULT_FILE_STORAGE', 'N/A'),
        'MEDIA_URL': django_settings.MEDIA_URL,
        'has_AWS_ACCESS_KEY_ID': hasattr(django_settings, 'AWS_ACCESS_KEY_ID'),
        'keys_from_os': (os.environ.get('S3_ACCESS_KEY', '')[:8] + '...') if os.environ.get('S3_ACCESS_KEY') else 'NONE',
        'keys_from_config': (django_settings.AWS_ACCESS_KEY_ID[:8] + '...') if hasattr(django_settings, 'AWS_ACCESS_KEY_ID') else 'N/A',
        'python_path': str(sys.path[:3]),
    })
