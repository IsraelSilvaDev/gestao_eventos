# Gerenciar Convites — CRUD de Convites

## Visão Geral

Página para o organizador gerenciar convites de um evento: criar, listar, filtrar, copiar link, excluir.

## Responsabilidades

- Listar convites com código, destinatário e status
- Criar convite individual via modal
- Filtrar por status (confirmado, declinado, respondido)
- Copiar link e compartilhar via WhatsApp
- Excluir convite

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Listar convites com código, destinatário, status, resposta | Must |
| RF-02 | Criar convite individual via modal Bootstrap | Must |
| RF-03 | Filtro rápido por status (cards clicáveis) | Should |
| RF-04 | Copiar código do convite | Should |
| RF-05 | Copiar link do convite | Should |
| RF-06 | Compartilhar via WhatsApp | Should |
| RF-07 | Excluir convite com modal de confirmação | Must |
| RF-08 | Exibir 3 stat cards: confirmados, respondidos, declinados | Should |
| RF-09 | Link para criação múltipla | Should |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:262-293` | `gerenciar_convites_view` | 🟢 |
| `templates/dashboard/gerenciar_convites.html` | Template + JS | 🟢 |
