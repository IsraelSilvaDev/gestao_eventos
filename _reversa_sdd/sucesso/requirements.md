# Sucesso — Página de Confirmação

## Visão Geral

Página estática de agradecimento exibida após o convidado enviar ou atualizar sua resposta RSVP.

## Responsabilidades

- Exibir mensagem de confirmação de presença
- Oferecer link para voltar à página inicial

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Exibir mensagem "Presença confirmada com sucesso!" após resposta | Must | Texto visível no centro da página |
| RF-02 | Exibir link "Voltar ao início" | Should | Link para `/` |

## Rastreabilidade de Código

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:97-99` | `sucesso_view` | 🟢 |
| `templates/sucesso.html` | Template | 🟢 |
