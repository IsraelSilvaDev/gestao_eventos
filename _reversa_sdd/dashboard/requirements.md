# Dashboard — Painel do Organizador

## Visão Geral

Página principal do organizador com visão geral de todos os eventos, estatísticas globais e gráficos.

## Responsabilidades

- Exibir estatísticas globais (total convites, respondidos, pendentes, taxa)
- Exibir gráfico doughnut (confirmados × declinados × pendentes)
- Exibir gráfico de barras (convites por evento)
- Listar eventos com busca, filtro e ordenação
- Fornecer ações rápidas (ver, editar, copiar link, WhatsApp)

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Exibir 4 stat cards com animação | Must |
| RF-02 | Gráfico doughnut com Chart.js | Must |
| RF-03 | Gráfico barras com Chart.js | Must |
| RF-04 | Tabela de eventos com busca textual | Must |
| RF-05 | Filtro por status (com confirmados / pendentes) | Should |
| RF-06 | Ordenação por coluna (nome, data, convites) | Should |
| RF-07 | Copiar link do evento via clipboard | Should |
| RF-08 | Compartilhar via WhatsApp | Should |
| RF-09 | Botão "Novo Evento" | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:108-149` | `dashboard_view` | 🟢 |
| `templates/dashboard/dashboard.html` | Template + Chart.js + JS | 🟢 |
