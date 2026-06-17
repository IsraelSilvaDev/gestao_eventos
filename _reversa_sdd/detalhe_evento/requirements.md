# Detalhe Evento — Respostas do Evento

## Visão Geral

Página de detalhes de um evento com lista de respostas e resumo estatístico.

## Responsabilidades

- Exibir resumo do evento
- Listar todas as respostas com status e acompanhantes
- Exibir total de pessoas confirmadas
- Mostrar botão para gerenciar convites

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Apenas organizador dono do evento pode acessar | Must |
| RF-02 | Exibir soma de total_pessoas dos confirmados | Must |
| RF-03 | Exibir contagem de confirmados e declinados | Must |
| RF-04 | Exibir lista de respostas ordenadas por data (decrescente) | Must |
| RF-05 | Exibir convites pendentes (sem resposta) | Must |
| RF-06 | Link para gerenciar convites do evento | Should |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:189-219` | `detalhe_evento_dashboard_view` | 🟢 |
| `templates/dashboard/detalhe_evento.html` | Template | 🟢 |
