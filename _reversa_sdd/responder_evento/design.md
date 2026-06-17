# Responder Evento, Design Técnico

## Interface

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/evento/<codigo_acesso>` | `codigo_acesso: str` | HTML | 200, 404 |
| POST | `/evento/<codigo_acesso>` | Form + `desmarcar?` | Redirect ou HTML | 302, 200 |

### Campos do POST

| Campo | Tipo | Obrigatório | Observação |
|-------|------|-------------|------------|
| `nome_principal` | string | Sim | Nome do convidado |
| `status` | string | Sim | "confirmado" ou "declinado" |
| `total_pessoas` | int | Sim | Default 1. 0 se declinado |
| `observacoes` | string | Não | Texto livre |
| `acompanhante_nome[]` | string[] | Condicional | Se confirmado e total_pessoas > 1 |
| `acompanhante_doc[]` | string[] | Condicional | Se confirmado e total_pessoas > 1 |
| `desmarcar` | string | Não | Se presente, cancela resposta |

## Fluxo Principal (GET)

1. Busca `Convite` por `codigo_acesso` ou 404 🟢 (`views.py:31`)
2. Obtém `evento = convite.evento` 🟢 (`views.py:32`)
3. Se `hasattr(convite, 'resposta')`: 🟢 (`views.py:79-83`)
   - Instancia `RespostaForm(instance=resposta)` 🟢 (`views.py:81`)
   - Busca `resposta.acompanhantes.all()` 🟢 (`views.py:82`)
   - Seta `ja_respondeu = True` 🟢
4. Senão: form vazio, lista vazia, `ja_respondeu = False` 🟢 (`views.py:84-87`)
5. Renderiza `responder_evento.html` com context 🟢 (`views.py:89-95`)

## Fluxo Principal (POST)

1. Se `desmarcar in request.POST`: 🟢 (`views.py:35`)
   - Deleta `resposta.acompanhantes.all()` 🟢 (`views.py:38`)
   - Deleta `resposta` 🟢 (`views.py:39`)
   - Messages success + redirect 🟢 (`views.py:40-41`)
2. Se `hasattr(convite, 'resposta')` (update): 🟢 (`views.py:43`)
   - Instancia `RespostaForm(request.POST, instance=resposta)` 🟢 (`views.py:45`)
   - Se válido: `form.save()` → delete + recreate companions 🟢 (`views.py:47-58`)
3. Senão (create): 🟢 (`views.py:61-77`)
   - Instancia `RespostaForm(request.POST)` 🟢 (`views.py:62`)
   - Se válido: `form.save(commit=False)` → `response.convite = convite` → save → create companions 🟢 (`views.py:63-76`)

## Fluxos Alternativos

- **Form inválido:** Renderiza página com erros de validação 🟢
- **Desmarcar sem resposta:** Apenas redirect (hasattr é falso) 🟢
- **Nome de acompanhante vazio:** Ignorado no loop (`if nome.strip()`) 🟢 (`views.py:53`)

## Dependências

- `Convite`, `Resposta`, `Acompanhante` (models)
- `RespostaForm` (form com validation custom)
- `evento` (para exibir detalhes)
- Bootstrap modal (para confirmação de desmarcar)
- JavaScript (para campos dinâmicos de acompanhantes)

## Decisões de Design

| Decisão | Evidência | Confiança |
|---------|-----------|-----------|
| Acompanhantes deletados e recriados (abordagem replace-all) | `views.py:48,68` | 🟢 |
| Modal Bootstrap para confirmar desmarcar | `responder_evento.html:140-161` | 🟢 |
| JS inline no template para dinamismo | `responder_evento.html:166-240` | 🟢 |
| Status como radio buttons com estilo btn-check | `responder_evento.html:70-98` | 🟢 |

## Estado Interno

- Resposta: persistido no banco via ORM
- Acompanhantes: persistido no banco, deletado+recriado a cada update
- Sessão: não usada (convite identificado por URL)

## Riscos e Lacunas

- 🔴 **Sem transação atômica:** Se a criação de acompanhantes falha após salvar a resposta, dados ficam inconsistentes
- 🔴 **Concorrência:** Dois POSTs simultâneos podem causar perda de dados de acompanhantes
- 🟡 **Validação de documento frágil:** Apenas HTML required, sem validação de formato CPF/RG
