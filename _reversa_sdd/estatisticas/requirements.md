# Estatísticas — Tabela de Dados por Evento

## Visão Geral

Página com tabela detalhada de estatísticas por evento, em formato de relatório.

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Exibir totais globais (convites, respondidos, pendentes, confirmados, declinados) | Must |
| RF-02 | Exibir tabela por evento com nome, total, respondidos, pendentes, confirmados, declinados | Must |
| RF-03 | Filtrar eventos do organizador logado | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:151-186` | `estatisticas_dashboard_view` | 🟢 |
| `templates/dashboard/estatisticas.html` | Template | 🟢 |
