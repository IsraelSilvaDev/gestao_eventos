# Relatório de Confiança — Gestão de Eventos

> Gerado pelo Revisor em 2026-06-17

---

## Resumo Geral

| Nível | Quantidade | Percentual |
|-------|-----------|------------|
| 🟢 CONFIRMADO | 185 | 85.3% |
| 🟡 INFERIDO | 14 | 6.4% |
| 🔴 LACUNA | 18 | 8.3% |
| **Total** | **217** | **100%** |

**Confiança geral: 88.5%** (🟢 + metade dos 🟡)

---

## Por Spec

| Spec | 🟢 | 🟡 | 🔴 | Confiança |
|------|----|----|-----|-----------|
| home | 26 | 4 | 5 | 80.0% |
| responder_evento | 48 | 2 | 4 | 90.7% |
| sucesso | 4 | 0 | 0 | 100% |
| login | 10 | 0 | 1 | 90.9% |
| logout | 7 | 0 | 0 | 100% |
| criar_evento | 10 | 0 | 0 | 100% |
| editar_evento | 8 | 0 | 0 | 100% |
| detalhe_evento | 9 | 0 | 0 | 100% |
| dashboard | 19 | 3 | 2 | 85.4% |
| estatisticas | 7 | 0 | 0 | 100% |
| gerenciar_convites | 11 | 0 | 0 | 100% |
| criar_convites_multiplos | 7 | 0 | 0 | 100% |
| excluir_convite | 6 | 0 | 0 | 100% |
| gerar_link_convite | 4 | 0 | 0 | 100% |
| domain.md (global) | 10 | 4 | 5 | 63.2% |
| permissions.md (global) | 3 | 1 | 1 | 70.0% |

---

## Lacunas Pendentes 🔴

Itens que permaneceram sem confirmação após a revisão:

### home
- **RF-05 — Exibir detalhes do evento na home** — não implementado no código atual. Mantido como Could aspiracional. (`home/requirements.md:27`)
- **Sem proteção contra brute force** — `views.py:14-27` não tem rate limiting. (`home/requirements.md:33`)
  - Pergunta correspondente: review session

### dashboard
- **BUG `convites.first().codigo_acesso`** — causa AttributeError se evento não tiver convites. (`dashboard/design.md:38, views.py:137`)
- **Dados inline no HTML** — pode ficar pesado com dezenas de eventos. (`dashboard/design.md:39`)

### domain.md
- **L01 — Auditoria** — sem log de operações CRUD. Priorizado para correção.
- **L02 — Validação de documento** — sem formato. Priorizado para correção.
- **L03 — Privacidade de dados** — sem proteção especial. Priorizado para correção.
- **L04 — Testes** — cobertura zero. Planejado.
- **RB10 — Evento precisa de ao menos um convite para gerar link** — inferido, confirmado como bug. (`domain.md:62`)

---

## Recomendações

- [ ] **dashboard**: Corrigir bug `convites.first().codigo_acesso` — adicionar guarda `if convites.exists()` (`views.py:137`)
- [ ] **home/login**: Avaliar necessidade de rate limiting contra brute force
- [ ] **Geral**: Implementar auditoria, validação de documento e proteção de dados conforme priorizado
- [ ] **Geral**: Escrever testes para fluxos principais (RSVP, criação de evento, geração de convites)

---

## Histórico de Reclassificações

| De | Para | Afirmação | Motivo |
|----|------|-----------|--------|
| 🟢 | 🔴 | RF-05 — Exibir detalhes do evento na home | Não existe no código — reclassificado como Lacuna |
| 🔴 | 🟢 | L04 — tests.py vazio | Confirmado pelo usuário como verdade conhecida |
| 🟡 | 🔴 | RB10 — Evento precisa de ao menos um convite | Usuário confirmou como bug a corrigir |

---

## Checkpoint da Revisão

| Métrica | Valor |
|---------|-------|
| Unidades revisadas | 14 |
| Arquivos revisados | 48 |
| Revisão cruzada | Não realizada (Codex indisponível) |
| Reclassificações | 3 |
| Perguntas feitas ao usuário | 4 |
| Respostas obtidas | 4 |
| Gaps documentados | 8 (2 críticos, 4 moderados, 2 cosméticos) |
| Confiança geral final | 88.5% |
