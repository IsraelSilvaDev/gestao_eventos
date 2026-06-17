# Legacy Impact — Corrigir Filtro das Estatísticas Globais no Dashboard

> Gerado em 2026-06-17
> Feature: `001-corrigir-estatisticas-dashboard`

---

## Arquivos e Componentes Afetados

| Arquivo | Componente | Tipo | Severidade | Justificativa |
|---------|-----------|------|------------|---------------|
| `eventos/views.py:114-119` | `dashboard_view` | regra-alterada | HIGH | Queries de agregação global passam a filtrar por organizador |
| `eventos/views.py:122-123` | `dashboard_view` | regra-alterada | MEDIUM | Taxa recalcula com novos totais (efeito colateral) |
| `eventos/views.py:155-160` | `estatisticas_dashboard_view` | regra-alterada | HIGH | Queries de agregação global passam a filtrar por organizador |

## Diff Conceitual

### dashboard_view

**Antes:**
```
Convite.objects.count() → total global do sistema
Resposta.objects.filter(status='confirmado').count() → respostas de todos os eventos
```

**Depois:**
```
Convite.objects.filter(evento__organizador=request.user).count() → apenas do organizador
Resposta.objects.filter(convite__evento__organizador=request.user, status='confirmado').count()
```

O comportamento do loop `for evento in eventos` (per-event stats) não foi alterado.

### estatisticas_dashboard_view

Mesma alteração: queries de agregação global filtram por `evento__organizador=request.user`. As stats por evento dentro do loop permanecem intactas.

## Preservadas

| Regra | Fonte | Confiança |
|-------|-------|-----------|
| RB02 — Uma resposta por convite | `domain.md#RB02` | 🟢 |
| RB03 — Validação de pessoa por status | `domain.md#RB03` | 🟢 |
| RB04 — Acompanhantes vinculados à resposta | `domain.md#RB04` | 🟢 |
| RB05 — Acompanhantes são destrutivos | `domain.md#RB05` | 🟢 |
| RB06 — Confirmação zera ao recusar | `domain.md#RB06` | 🟢 |
| RB07 — Confirmação não edita acompanhantes | `domain.md#RB07` | 🟢 |
| RB08 — Geração de código único | `domain.md#RB08` | 🟢 |
| RB09 — Desmarcar volta a pendente | `domain.md#RB09` | 🟢 |
| RB11 — Sem confirmação por lote | `domain.md#RB11` | 🟡 |
| RB12 — Sem notificações automáticas | `domain.md#RB12` | 🟡 |
| RB13 — Sem controle de vagas | `domain.md#RB13` | 🟡 |
| Per-event stats corretas | `dashboard/design.md` | 🟢 |

## Modificadas

| Regra | Fonte | Antes | Depois | Confiança |
|-------|-------|-------|--------|-----------|
| RB01 — Organizador só vê seus dados | Nova (inferida do bug) | Não existia — global stats mostravam dados de todos | Global stats filtradas por organizador | 🟢 |
| RB10 — Evento precisa de convite para link | `domain.md#RB10` | 🟡 Inferido como risco | 🟢 Confirmado — guarda `if convites.exists()` existe | 🟢 |
