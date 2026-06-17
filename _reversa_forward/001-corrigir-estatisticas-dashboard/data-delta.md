# Data Delta — Corrigir Filtro das Estatísticas

## Modelo de Dados

Sem alterações. Nenhum campo novo, tabela nova ou migração necessária. A correção é puramente no escopo das queries (restrição de linhas retornadas).

## Impacto Esperado

| Métrica | Antes (bug) | Depois (corrigido) |
|---------|-------------|-------------------|
| Total convites no dashboard | Global (todos organizadores) | Apenas do organizador logado |
| Respondidos no dashboard | Global | Apenas do organizador logado |
| Pendentes no dashboard | Global | Apenas do organizador logado |
| Confirmados no dashboard | Global | Apenas do organizador logado |
| Declinados no dashboard | Global | Apenas do organizador logado |
| Taxa de resposta | Baseada em dados globais | Baseada apenas nos eventos do organizador |
| Per-event stats | Corretas (filtradas) | Inalteradas |

## Migrações

Nenhuma migração de banco necessária.
