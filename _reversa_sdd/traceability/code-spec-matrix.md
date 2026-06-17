# Matriz de Cobertura Código × Specs

## Arquivos do Legado vs. Units

| Arquivo do legado | Unit correspondente | Cobertura |
|-------------------|---------------------|-----------|
| `eventos/models.py` | Transversal (data-dictionary.md) | 🟢 |
| `eventos/views.py:12-27` (home_view) | `home/` | 🟢 |
| `eventos/views.py:29-95` (responder_evento_view) | `responder_evento/` | 🟢 |
| `eventos/views.py:97-99` (sucesso_view) | `sucesso/` | 🟢 |
| `eventos/views.py:104-106` (is_organizador) | Transversal (permissions.md) | 🟢 |
| `eventos/views.py:108-149` (dashboard_view) | `dashboard/` | 🟢 |
| `eventos/views.py:151-186` (estatisticas_dashboard_view) | `estatisticas/` | 🟢 |
| `eventos/views.py:189-219` (detalhe_evento_dashboard_view) | `detalhe_evento/` | 🟢 |
| `eventos/views.py:221-242` (criar_evento_view) | `criar_evento/` | 🟢 |
| `eventos/views.py:245-260` (editar_evento_view) | `editar_evento/` | 🟢 |
| `eventos/views.py:262-293` (gerenciar_convites_view) | `gerenciar_convites/` | 🟢 |
| `eventos/views.py:296-325` (criar_convites_multiplos_view) | `criar_convites_multiplos/` | 🟢 |
| `eventos/views.py:328-335` (excluir_convite_view) | `excluir_convite/` | 🟢 |
| `eventos/views.py:338-342` (gerar_link_convite_view) | `gerar_link_convite/` | 🟢 |
| `eventos/forms.py:4-11` (CodigoAcessoForm) | `home/` | 🟢 |
| `eventos/forms.py:13-53` (RespostaForm) | `responder_evento/` | 🟢 |
| `eventos/forms.py:55-79` (EventoForm) | `criar_evento/`, `editar_evento/` | 🟢 |
| `eventos/forms.py:81-93` (ConviteForm) | `gerenciar_convites/` | 🟢 |
| `eventos/forms.py:95-116` (ConviteMultiploForm) | `criar_convites_multiplos/` | 🟢 |
| `eventos/urls.py` | Transversal (roteamento) | 🟢 |
| `eventos/admin.py` | n/a (Django built-in) | n/a |
| `gestao_eventos/urls.py` | Transversal (roteamento raiz) | 🟢 |
| `gestao_eventos/settings.py` | n/a (config de projeto) | n/a |
| `templates/base.html` | Transversal (layout base) | 🟢 |
| `templates/home.html` | `home/` | 🟢 |
| `templates/responder_evento.html` | `responder_evento/` | 🟢 |
| `templates/sucesso.html` | `sucesso/` | 🟢 |
| `templates/registration/login.html` | `login/` | 🟢 |
| `templates/dashboard/dashboard.html` | `dashboard/` | 🟢 |
| `templates/dashboard/detalhe_evento.html` | `detalhe_evento/` | 🟢 |
| `templates/dashboard/estatisticas.html` | `estatisticas/` | 🟢 |
| `templates/dashboard/form_evento.html` | `criar_evento/`, `editar_evento/` | 🟢 |
| `templates/dashboard/gerenciar_convites.html` | `gerenciar_convites/` | 🟢 |
| `templates/dashboard/criar_convites_multiplos.html` | `criar_convites_multiplos/` | 🟢 |
| `templates/admin/index.html` | n/a (Django admin) | n/a |
| `templates/admin/estatisticas.html` | n/a (Django admin) | n/a |
| `gestao_eventos/wsgi.py` | n/a (infra) | n/a |
| `gestao_eventos/asgi.py` | n/a (infra) | n/a |
| `manage.py` | n/a (entry point) | n/a |

## Resumo

| Métrica | Valor |
|---------|-------|
| Total arquivos .py (app) | 6 (urls, views, models, forms, admin, tests) |
| Cobertos por alguma unit | 5 (83%) |
| Não cobertos | admin.py (Django admin config), tests.py (vazio) |
| Total templates | 13 |
| Cobertos por alguma unit | 13 (100%) |
