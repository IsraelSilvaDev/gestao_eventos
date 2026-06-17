# Logout, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| POST | `/logout/` | CSRF token | Redirect | 302 |
| GET | `/logout/` | — | 405 | 405 (Method Not Allowed) |

Usa `django.contrib.auth.views.LogoutView`. Config:
- `LOGOUT_REDIRECT_URL = 'home'` 🟢 (`settings.py:81`)
- Botão de logout fica na navbar, dentro de `<form method="post">` 🟢 (`base.html:47-49`)

## Dependências

- Django `contrib.auth`
- CSRF middleware
