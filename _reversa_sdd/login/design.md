# Login, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/login/` | — | HTML | 200 |
| POST | `/login/` | username, password | Redirect | 302 (sucesso), 200 (erro) |

Usa `django.contrib.auth.views.LoginView` com template customizado. Configurações:
- `template_name`: `registration/login.html` 🟢 (`urls.py:12`)
- `LOGIN_REDIRECT_URL`: `dashboard` 🟢 (`settings.py:80`)

## Dependências

- Django `contrib.auth` (built-in)
- Template `registration/login.html`
- Config `LOGIN_URL = 'login'`

## Decisões de Design

| Decisão | Evidência | Confiança |
|---------|-----------|-----------|
| Usa LoginView padrão do Django, sem customização | `eventos/urls.py:12` | 🟢 |
| Template Bootstrap customizado em vez do padrão | `urls.py:12` (template_name) | 🟢 |
| Sem rate limiting no login | — | 🔴 |
