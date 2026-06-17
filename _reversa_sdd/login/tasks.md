# Login, Tarefas

- [ ] T-01, Criar template `registration/login.html` com Bootstrap
  - Origem: `templates/registration/login.html`
  - Critério de pronto: Formulário com username, password, botão "Entrar"
  - Confiança: 🟢

- [ ] T-02, Configurar URL com `LoginView.as_view(template_name=...)`
  - Origem: `eventos/urls.py:12`
  - Critério de pronto: GET /login/ → template customizado
  - Confiança: 🟢

- [ ] T-03, Configurar `LOGIN_REDIRECT_URL = 'dashboard'`
  - Origem: `gestao_eventos/settings.py:80`
  - Critério de pronto: Após login, redireciona para /dashboard/
  - Confiança: 🟢
