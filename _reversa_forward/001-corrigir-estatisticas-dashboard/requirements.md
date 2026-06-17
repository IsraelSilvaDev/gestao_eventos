# Corrigir Filtro das Estatísticas Globais no Dashboard

## Visão Geral

As estatísticas globais exibidas nos cards do dashboard e na página de estatísticas mostram dados de **todos os convites do sistema**, independentemente de qual organizador criou o evento. Isso viola o isolamento esperado entre organizadores — cada organizador deve ver apenas dados dos seus próprios eventos.

**Referência:** `_reversa_sdd/dashboard/design.md#L7-L15`, `_reversa_sdd/gaps.md#G01`, `_reversa_sdd/domain.md#RB10`

## Escopo

**Dentro:**
- `dashboard_view` — filtrar `Convite.objects.count()` e `Resposta.objects.filter()` por eventos do organizador logado
- `estatisticas_dashboard_view` — mesma correção nas queries de linha 155-160
- Template `dashboard/dashboard.html` — não requer alteração (contexto mantém mesmas chaves)
- Template `dashboard/estatisticas.html` — não requer alteração

**Fora:**
- Alteração no modelo de dados
- Mudança na estrutura do template
- Correção do `convites.first().codigo_acesso` (já possui guarda `if convites.exists()` em `views.py:137`)
- Outros bugs ou features

## Regras de Negócio

- RB01 — Organizador só vê dados dos seus próprios eventos 🟢 (`_reversa_sdd/domain.md#RB01`, confirmado pelo padrão `Evento.objects.filter(organizador=request.user)` em `views.py:112`)
- RB02 — Global stats devem refletir apenas convites dos eventos do organizador 🟡 (inferido: é a correção desejada, mas não há regra explícita no código atual)

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Dashboard: `total_convites` filtrar por eventos do organizador | Must | `Convite.objects.filter(evento__organizador=request.user).count()` |
| RF-02 | Dashboard: `convites_respondidos` filtrar por eventos do organizador | Must | Mesmo filtro com `resposta__isnull=False` |
| RF-03 | Dashboard: `convites_pendentes` filtrar por eventos do organizador | Must | Mesmo filtro com `resposta__isnull=True` |
| RF-04 | Dashboard: `confirmados` filtrar por eventos do organizador | Must | `Resposta.objects.filter(convite__evento__organizador=request.user, status='confirmado').count()` |
| RF-05 | Dashboard: `declinados` filtrar por eventos do organizador | Must | Mesmo filtro com `status='declinado'` |
| RF-06 | Dashboard: `taxa_resposta` recalcular com dados filtrados | Must | Taxa = respondidos_do_organizador / total_do_organizador |
| RF-07 | Estatísticas: aplicar os mesmos 5 filtros nas queries globais | Must | `estatisticas_dashboard_view` linhas 155-160 |
| RF-08 | Per-event stats permanecem inalteradas | Must | Loop `for evento in eventos` já filtra por `organizador` via `evento.convites.all()` |

## Arquivos Afetados

| Arquivo | Função | Mudança |
|---------|--------|---------|
| `eventos/views.py:110-149` | `dashboard_view` | 6 queries a corrigir (linhas 114-119, 122-123) |
| `eventos/views.py:153-186` | `estatisticas_dashboard_view` | 5 queries a corrigir (linhas 155-160) |

## Riscos

- 🟡 **Performance**: Adicionar join via `evento__organizador` pode aumentar tempo de query em sistemas com muitos eventos. Mitigação: índice em `Convite.evento` já existe (FK) e cascade `evento__organizador` é lookup direto.
- 🟢 **Regressão**: Nenhum risco de regressão — código atual está incorreto, correção só restringe escopo dos dados.

## Notas

O bug foi identificado durante a revisão cruzada do Reversa. O código atual usa `Convite.objects.count()` (sem filtro) nas views `dashboard_view:114` e `estatisticas_dashboard_view:155`. A correção consiste em adicionar o filtro `.filter(evento__organizador=request.user)` nas queries de agregação global.
