# Roadmap — Corrigir Filtro das Estatísticas Globais no Dashboard

## Resumo da Abordagem

Correção de escopo puramente nas queries ORM das views `dashboard_view` e `estatisticas_dashboard_view`. Nenhuma alteração em modelos, templates, formulários ou banco de dados. A correção consiste em adicionar o filtro `evento__organizador=request.user` nas 6 queries de agregação global do dashboard e 5 queries da página de estatísticas.

## Delta Arquitetural

Nenhum. O padrão arquitetural (server-rendered, form-based, monolítico) permanece inalterado. Apenas o escopo dos dados nas queries é restringido.

**Arquivos tocados:**

| Arquivo | Linhas | Mudança |
|---------|--------|---------|
| `eventos/views.py:114-119` | 6 | Adicionar `Convite.objects.filter(evento__organizador=request.user)` |
| `eventos/views.py:122-123` | 2 | Taxa recalcula automaticamente com novos totais |
| `eventos/views.py:155-160` | 6 | Mesmo filtro na view de estatísticas |

## Decisões Técnicas

- DT01 — **Filtro via ORM com join implícito**: usar `Convite.objects.filter(evento__organizador=request.user)` em vez de subquery. O Django ORM traduz para `INNER JOIN eventos_evento ON (eventos_convite.evento_id = eventos_evento.id) WHERE eventos_evento.organizador_id = <id>`. Performance aceitável com índices existentes (FK `evento_id` e FK `organizador_id`). 🟢
- DT02 — **Não extrair para variável compartilhada**: as duas views são independentes; cada uma tem seu próprio conjunto de queries. Extrair para função auxiliar seria over-engineering para 6 queries simples. 🟢
- DT03 — **Não criar service layer**: a complexidade atual não justifica camada extra. Manter a lógica nas views é consistente com o resto da codebase. 🟢

## Delta de Dados

Nenhum. O modelo de dados não é alterado.

## Delta de Contratos

Nenhum. As chaves do contexto (`total_convites`, `convites_respondidos`, etc.) permanecem as mesmas. Templates não requerem alteração.

## Plano de Migração / Rollout

1. Editar `dashboard_view` (6 queries + taxa)
2. Editar `estatisticas_dashboard_view` (5 queries)
3. Verificar visualmente no navegador que os números mudaram (devem ser menores ou iguais aos anteriores)
4. Rodar `python manage.py test` (só para confirmar que não quebrou nada — sem testes específicos ainda)

## Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Query mais lenta com JOIN extra | Baixa | Baixo | FK indexada, volume atual pequeno |
| Esquecer de filtrar uma query | Média | Médio | Checklist: 11 queries no total (6+5) |
| Regression em per-event stats | Muito Baixa | Alto | Loop `for evento in eventos` não é alterado |

## Critério de Pronto

- [ ] `dashboard_view`: todas as 6 queries filtram por `evento__organizador=request.user`
- [ ] `estatisticas_dashboard_view`: todas as 5 queries filtram por `evento__organizador=request.user`
- [ ] Organizador A vê apenas dados dos seus eventos no dashboard
- [ ] Organizador A vê apenas dados dos seus eventos na página de estatísticas
- [ ] Per-event stats continuam funcionando normalmente
- [ ] `python manage.py test` não quebra
