# Logout, Tarefas

- [ ] T-01, Configurar URL com `LogoutView.as_view()`
  - Origem: `eventos/urls.py:13`
  - Critério de pronto: POST /logout/ → 302 para home
  - Confiança: 🟢

- [ ] T-02, Configurar `LOGOUT_REDIRECT_URL = 'home'`
  - Origem: `gestao_eventos/settings.py:81`
  - Critério de pronto: Após logout, redireciona para /
  - Confiança: 🟢

- [ ] T-03, Adicionar botão de logout na navbar (POST form)
  - Origem: `templates/base.html:47-49`
  - Critério de pronto: Navbar exibe "Sair" para staff logado
  - Confiança: 🟢
