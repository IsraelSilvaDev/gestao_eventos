# Home, Design Técnico

## Interface

| Método | Caminho | Entrada | Saída | Status codes |
|--------|---------|---------|-------|--------------|
| GET | `/` | — | HTML (home.html) | 200 |
| POST | `/` | `codigo: str (max 8)` | Redirect ou HTML | 302, 200 (com erro) |

## Fluxo Principal

1. GET / → Renderiza `home.html` com `CodigoAcessoForm` vazio 🟢 (`eventos/views.py:24-27`)
2. POST / → Instancia `CodigoAcessoForm(request.POST)` 🟢 (`eventos/views.py:16`)
3. Form válido? Se não → renderiza com erros 🟢 (`eventos/views.py:17`)
4. Converte código para uppercase 🟢 (`eventos/views.py:18`)
5. Busca `Convite.objects.get(codigo_acesso=codigo)` 🟢 (`eventos/views.py:20`)
6. Encontrado? → redirect `responder_evento` com código 🟢 (`eventos/views.py:21`)
7. Não encontrado? → `Convite.DoesNotExist` → messages.error + render 🟢 (`eventos/views.py:22-23`)

## Fluxos Alternativos

- **Código inválido:** Captura `Convite.DoesNotExist`, exibe alerta de erro via Django messages framework 🟢
- **Código com espaços:** O Django Form limpa espaços automaticamente via `cleaned_data` 🟡

## Dependências

- `Convite` (model), validação de existência do código
- `CodigoAcessoForm` (form), validação de formato do código
- Django Messages Framework, exibição de feedback

## Decisões de Design Identificadas

| Decisão | Evidência no código | Confiança |
|---------|---------------------|-----------|
| Código convertido para uppercase na view, não no form | `eventos/views.py:18` | 🟢 |
| Uso de messages.error em vez de form.add_error | `eventos/views.py:23` | 🟢 |
| Sem rate limiting ou throttle na busca | — | 🔴 |

## Estado Interno

Stateless — não mantém estado entre requisições.

## Observabilidade

- Logs padrão do Django para requisições (não customizado)
- Messages error são o único feedback visível para o usuário

## Riscos e Lacunas

- 🔴 **Sem rate limiting:** Um atacante pode enumerar códigos de convite via brute force
- 🟡 **Sem transação:** A view não usa `select_for_update()` — race condition teórica se o convite for excluído entre o GET e o POST
