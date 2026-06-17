# Regression Watch — Corrigir Filtro das Estatísticas Globais no Dashboard

> Gerado em 2026-06-17
> Feature: `001-corrigir-estatisticas-dashboard`

---

## Itens de Regressão

| ID | Origem | Regra Esperada | Tipo | Sinal de Violação |
|----|--------|---------------|------|-------------------|
| W001 | `eventos/views.py:114-119`, `dashboard_view` | `total_convites` conta apenas convites dos eventos do organizador logado | presença | `Convite.objects.count()` sem filtro `evento__organizador` |
| W002 | `eventos/views.py:114-119`, `dashboard_view` | `convites_respondidos` conta apenas respondidos dos eventos do organizador | presença | `Convite.objects.filter(resposta__isnull=False)` sem filtro de organizador |
| W003 | `eventos/views.py:114-119`, `dashboard_view` | `convites_pendentes` conta apenas pendentes dos eventos do organizador | presença | `Convite.objects.filter(resposta__isnull=True)` sem filtro de organizador |
| W004 | `eventos/views.py:118-119`, `dashboard_view` | `confirmados` e `declinados` filtram por `convite__evento__organizador` | presença | `Resposta.objects.filter(status=...)` sem join com `convite__evento` |
| W005 | `eventos/views.py:155-160`, `estatisticas_dashboard_view` | Mesmas 5 regras acima na view de estatísticas | presença | Qualquer `Convite.objects.count()` sem filtro em `estatisticas_dashboard_view` |

## Histórico de Re-extrações

*(A ser preenchido pelo agente reverso quando `/reversa` rodar novamente)*

## Arquivadas

*(Nenhuma no momento)*

## Observações

- Itens W001-W005 verificam que queries usam `evento__organizador=request.user`
- Regras RB11-RB13 (confirmação por lote, notificações, controle de vagas) permanecem 🟡 — não geram watch items
- Per-event stats dentro do loop `for evento in eventos` não foram alteradas e não requerem watch
