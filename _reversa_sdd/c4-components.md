# Diagrama C4 — Componentes (Nível 3)

## Container: Aplicação Web (Django)

```mermaid
C4Component
    title Diagrama de Componentes - Django App

    Container_Boundary(django, "Aplicação Web Django") {
        Component(urls, "URL Router", "eventos/urls.py + gestao_eventos/urls.py", "Roteia requisições para views")
        Component(views, "Views", "eventos/views.py", "12 view functions: home, RSVP, dashboard, CRUD")
        Component(forms, "Forms", "eventos/forms.py", "5 formulários: CodigoAcesso, Resposta, Evento, Convite, ConviteMultiplo")
        Component(models, "Models", "eventos/models.py", "4 modelos: Evento, Convite, Resposta, Acompanhante")
        Component(admin, "Admin Config", "eventos/admin.py", "Configura Django Admin para os 4 modelos")
        Component(auth, "Auth Views", "django.contrib.auth", "LoginView + LogoutView padrão")
        Component(templates, "Template Engine", "Django Templates", "13 templates Bootstrap 5")
    }

    ContainerDb(db, "Banco de Dados", "SQLite/PostgreSQL")

    Rel(urls, views, "Roteia")
    Rel(urls, auth, "Roteia")
    Rel(views, forms, "Instancia e valida")
    Rel(views, models, "Queries ORM")
    Rel(views, templates, "Renderiza")
    Rel(forms, models, "Salva dados")
    Rel(admin, models, "Configura admin")
    Rel(models, db, "ORM")
```

## Views por Tipo

### Públicas
| Componente | Rota | Template |
|-----------|------|----------|
| `home_view` | GET/POST `/` | home.html |
| `responder_evento_view` | GET/POST `/evento/<codigo>/` | responder_evento.html |
| `sucesso_view` | GET `/sucesso/` | sucesso.html |

### Autenticação
| Componente | Rota | Template |
|-----------|------|----------|
| `LoginView` | GET/POST `/login/` | registration/login.html |
| `LogoutView` | POST `/logout/` | — (redirect) |

### Dashboard (Staff)
| Componente | Rota | Template |
|-----------|------|----------|
| `dashboard_view` | GET `/dashboard/` | dashboard/dashboard.html |
| `estatisticas_dashboard_view` | GET `/dashboard/estatisticas/` | dashboard/estatisticas.html |
| `detalhe_evento_dashboard_view` | GET `/dashboard/evento/<id>/` | dashboard/detalhe_evento.html |
| `criar_evento_view` | GET/POST `/dashboard/criar/` | dashboard/form_evento.html |
| `editar_evento_view` | GET/POST `/dashboard/evento/<id>/editar/` | dashboard/form_evento.html |
| `gerenciar_convites_view` | GET/POST `/dashboard/evento/<id>/convites/` | dashboard/gerenciar_convites.html |
| `criar_convites_multiplos_view` | GET/POST `/dashboard/evento/<id>/convites/criar/` | dashboard/criar_convites_multiplos.html |
| `excluir_convite_view` | GET `/dashboard/convite/<id>/excluir/` | — (redirect) |
| `gerar_link_convite_view` | GET `/dashboard/convite/<id>/link/` | — (JSON) |
