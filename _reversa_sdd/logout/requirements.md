# Logout — Encerrar Sessão

## Visão Geral

Endpoint para encerrar a sessão do organizador. Aceita apenas POST por segurança.

## Responsabilidades

- Encerrar sessão do usuário
- Redirecionar para página inicial

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Aceitar apenas POST (CSRF protegido) | Must | GET retorna 405 |
| RF-02 | Encerrar sessão e redirecionar para home | Must | POST → 302 para / |

## Rastreabilidade de Código

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/urls.py:13` | `LogoutView.as_view()` | 🟢 |
| `gestao_eventos/settings.py:81` | `LOGOUT_REDIRECT_URL` | 🟢 |
