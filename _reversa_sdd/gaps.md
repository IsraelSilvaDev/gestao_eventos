# Lacunas — Gestão de Eventos

> Gerado pelo Revisor em 2026-06-17

---

## Resumo

| Severidade | Quantidade | Descrição |
|------------|-----------|-----------|
| 🔴 Crítico | 2 | Podem causar exceção em produção ou bloquear reimplementação |
| 🟡 Moderado | 4 | Impactam qualidade, mas não quebram funcionalidade principal |
| 🔵 Cosmético | 2 | Melhorias menores, sem impacto em comportamento |

---

## 🔴 Crítico

### G01 — AttributeError em dashboard se evento não tiver convites

**Arquivo:** `eventos/views.py:137`
**Spec:** `dashboard/design.md`
**Problema:** `convites.first().codigo_acesso` sem guarda — se `convites` queryset for vazio, `.first()` retorna `None` e `.codigo_acesso` levanta `AttributeError`.
**Correção sugerida:** Adicionar `if convites.exists()` antes de acessar o código.
**Status:** ✅ Confirmado para correção

### G02 — Sem rate limiting na página de login/home

**Arquivo:** `eventos/views.py:14-27, eventos/views.py:32-48`
**Spec:** `home/requirements.md`, `login/requirements.md`
**Problema:** O formulário de busca por código e o login não têm proteção contra brute force. Qualquer IP pode tentar códigos/senhas indefinidamente.
**Correção sugerida:** Adicionar `django-ratelimit` ou middleware de throttling.
**Status:** 📝 Documentado sem ação definida

---

## 🟡 Moderado

### G03 — Sem log de auditoria em CRUD de convites

**Arquivo:** `eventos/views.py` (gerenciar_convites, criar_convites_multiplos, excluir_convite)
**Spec:** `domain.md:80-82`
**Problema:** Não há registro de quem criou, editou ou excluiu convites. `data_resposta` com `auto_now` perde timestamp original.
**Correção sugerida:** Adicionar `django-simple-history` ou campos `created_by/updated_by` manuais.
**Status:** ✅ Priorizado para correção

### G04 — Validação insuficiente em `Acompanhante.documento`

**Arquivo:** `eventos/models.py` (campo `documento`)
**Spec:** `domain.md:84-86`
**Problema:** CharField(50) sem validação de formato — aceita CPF, CNPJ, ou qualquer string.
**Correção sugerida:** Adicionar validação com `django-localflavor` ou `validate_cpf` customizada.
**Status:** ✅ Priorizado para correção

### G05 — Sem proteção de dados pessoais

**Arquivo:** `eventos/models.py` (Convidado via Convite)
**Spec:** `domain.md:88-90`
**Problema:** Dados de convidados (nome, documento) sem proteção especial, sem política de retenção.
**Correção sugerida:** Adicionar campo `data_expiracao` e script de anonimização.
**Status:** ✅ Priorizado para correção

### G06 — Cobertura de testes zero

**Arquivo:** `eventos/tests.py`
**Spec:** `domain.md:92-93`
**Problema:** Nenhum teste automatizado.
**Correção sugerida:** Escrever testes para fluxos principais (RSVP, criação de evento, geração de convites).
**Status:** ✅ Planejado

---

## 🔵 Cosmético

### G07 — RF-05 aspiracional em home

**Arquivo:** `_reversa_sdd/home/requirements.md:27`
**Spec:** `home/requirements.md`
**Problema:** O requisito "Exibir detalhes do evento na página inicial" não está implementado — a home redireciona para `/evento/<codigo>/`.
**Status:** Mantido como Could para futuro

### G08 — Nomes de campos inconsistentes em forms

**Arquivo:** `eventos/forms.py`
**Spec:** Vários
**Problema:** `ConviteMultiploForm` usa `nomes` (plural) e `documentos` como lista textual; `ConviteForm` usa `nome` (singular) e `documento` — divergência pode confundir.
**Status:** 📝 Documentado sem ação definida
