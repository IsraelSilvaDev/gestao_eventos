# Inventário do Projeto — Gestão de Eventos

## Visão Geral

Sistema Django para gestão de eventos com criação de convites, RSVP online e dashboard para organizadores.

## Estrutura de Diretórios

```
gestao_eventos/              # Pacote de configuração do projeto Django
├── __init__.py
├── asgi.py                  # Entry point ASGI
├── settings.py              # Configurações do Django
├── urls.py                  # Roteamento raiz
├── wsgi.py                  # Entry point WSGI
└── wsgi_pa.py               # WSGI customizado para PythonAnywhere

eventos/                     # App principal (único)
├── __init__.py
├── admin.py                 # Configuração do admin
├── apps.py                  # EventosConfig
├── forms.py                 # 5 formulários
├── models.py                # 4 modelos
├── tests.py                 # Vazio (placeholder)
├── urls.py                  # 14 rotas
├── views.py                 # 12 view functions
└── migrations/              # 4 migrações

templates/                   # 13 templates HTML
├── base.html                # Layout base (Bootstrap 5)
├── home.html                # Página inicial — formulário de código
├── responder_evento.html    # Formulário RSVP
├── sucesso.html             # Confirmação
├── registration/
│   └── login.html           # Login do organizador
├── dashboard/
│   ├── dashboard.html       # Dashboard principal (Chart.js)
│   ├── detalhe_evento.html  # Detalhes do evento + respostas
│   ├── estatisticas.html    # Estatísticas por evento
│   ├── form_evento.html     # Criar/editar evento
│   ├── gerenciar_convites.html     # CRUD de convites
│   └── criar_convites_multiplos.html # Criação em lote
└── admin/
    ├── index.html           # Admin customizado
    └── estatisticas.html    # Estatísticas no admin

media/banners/2026/          # Banners de eventos enviados
staticfiles/                 # Arquivos estáticos coletados

gestao_eventos/ manage.py    # Gerenciador Django
requirements.txt             # Dependências
DOCUMENTACAO.md              # Documentação em português
DEPLOY_PYTHONANYWHERE.md     # Guia de deploy
```

## Tecnologias

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.x | Linguagem principal |
| Django | 6.0.3 | Framework web |
| Pillow | 12.2.0 | Manipulação de imagens (banners) |
| psycopg2-binary | 2.9.10 | Driver PostgreSQL |
| python-decouple | 3.8 | Leitura de `.env` |
| PostgreSQL | 16.14 | Banco de dados (via `.env`) |
| Bootstrap | 5.3.3 | Frontend (CDN) |
| Chart.js | 4.4.1 | Gráficos no dashboard (CDN) |
| Bootstrap Icons | 1.11.3 | Ícones (CDN) |

## Modelos de Dados

| Modelo | Tabela | Campos | Relacionamentos |
|--------|--------|--------|-----------------|
| Evento | eventos_evento | id, nome, data, local, descricao, banner, organizador (FK) | organizador -> User; convites -> Convite |
| Convite | eventos_convite | id, codigo_acesso (unique), nome_destinatario, evento (FK) | evento -> Evento; resposta -> Resposta (O2O) |
| Resposta | eventos_resposta | id, nome_principal, status, total_pessoas, observacoes, data_resposta, convite (O2O) | convite -> Convite; acompanhantes -> Acompanhante |
| Acompanhante | eventos_acompanhante | id, nome_completo, documento, resposta (FK) | resposta -> Resposta |

## Rotas

### Públicas
| Rota | View | Descrição |
|------|------|-----------|
| `/` | home_view | Formulário de código de acesso |
| `/evento/<codigo>/` | responder_evento_view | RSVP do convidado |
| `/sucesso/` | sucesso_view | Página de confirmação |
| `/login/` | auth_views.LoginView | Login |
| `/logout/` | auth_views.LogoutView | Logout (POST) |

### Dashboard (staff)
| Rota | View | Descrição |
|------|------|-----------|
| `/dashboard/` | dashboard_view | Dashboard com gráficos |
| `/dashboard/estatisticas/` | estatisticas_dashboard_view | Tabela de estatísticas |
| `/dashboard/criar/` | criar_evento_view | Criar evento |
| `/dashboard/evento/<id>/` | detalhe_evento_dashboard_view | Detalhes + respostas |
| `/dashboard/evento/<id>/editar/` | editar_evento_view | Editar evento |
| `/dashboard/evento/<id>/convites/` | gerenciar_convites_view | Gerenciar convites |
| `/dashboard/evento/<id>/convites/criar/` | criar_convites_multiplos_view | Criar convites em lote |
| `/dashboard/convite/<id>/excluir/` | excluir_convite_view | Excluir convite |
| `/dashboard/convite/<id>/link/` | gerar_link_convite_view | Link do convite (JSON) |
| `/admin/` | Django Admin | Admin padrão |

## Total de arquivos: 42 (excluindo venv, .git, __pycache__, media)
