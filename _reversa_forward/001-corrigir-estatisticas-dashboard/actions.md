# Actions — Corrigir Filtro das Estatísticas Globais no Dashboard

## Resumo

- Total de ações: 3
- Paralelizáveis: 2 (T002, T003)
- Maior cadeia de dependência: 2 níveis (T002 → T004, T003 → T004)

---

## Núcleo

| ID | Descrição | Dependências | Paralelismo | Arquivo alvo | Confidência | Status |
|----|-----------|-------------|-------------|--------------|-------------|--------|
| T001 | Corrigir `dashboard_view`: adicionar `Convite.objects.filter(evento__organizador=request.user)` nas 6 queries (linhas 114-119) e confirmar taxa (linhas 122-123) recalcula automaticamente | — | [//] | `eventos/views.py:110-149` | 🟢 | [X] |
| T002 | Corrigir `estatisticas_dashboard_view`: adicionar mesmo filtro nas 5 queries (linhas 155-160) | — | [//] | `eventos/views.py:153-186` | 🟢 | [X] |

## Polimento

| ID | Descrição | Dependências | Paralelismo | Arquivo alvo | Confidência | Status |
|----|-----------|-------------|-------------|--------------|-------------|--------|
| T003 | Verificar manualmente com 2 organizadores que os números do dashboard e estatísticas estão isolados (seguir `onboarding.md`) | T001, T002 | — | Navegador | 🟡 | [ ] |
