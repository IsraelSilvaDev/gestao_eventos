# Login — Autenticação do Organizador

## Visão Geral

Página de login para organizadores (staff) acessarem o dashboard.

## Responsabilidades

- Autenticar usuário via Django Auth
- Redirecionar para dashboard após sucesso
- Exibir erros de credenciais inválidas

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Exibir formulário de login (username + senha) | Must | Campos renderizados no template customizado |
| RF-02 | Autenticar e redirecionar para dashboard | Must | POST válido → 302 para /dashboard/ |
| RF-03 | Exibir erro para credenciais inválidas | Must | Mensagem "Usuário ou senha inválidos" |
| RF-04 | Usar template Bootstrap customizado | Must | Template `registration/login.html` em vez do padrão |

## Rastreabilidade de Código

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/urls.py:12` | `LoginView.as_view()` | 🟢 |
| `templates/registration/login.html` | Template | 🟢 |
| `gestao_eventos/settings.py:79-81` | `LOGIN_URL`, `LOGIN_REDIRECT_URL` | 🟢 |
