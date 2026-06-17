# Criar Convites Múltiplos, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/evento/<id>/convites/criar/` | — | HTML | 200 |
| POST | `/dashboard/evento/<id>/convites/criar/` | qtd, nome_base | Redirect | 302 |

1. GET: Renderiza `ConviteMultiploForm()` 🟢 (`views.py:318-319`)
2. POST: 🟢 (`views.py:301-316`)
   - `quantidade = form.cleaned_data['quantidade']` (1-50)
   - `nome_base = form.cleaned_data['nome_base'] or 'Convite'`
   - Loop `for i in range(quantidade)`: cria `Convite(nome_destinatario=f"{nome_base} {i+1}")`
   - Messages com quantidade + redirect
