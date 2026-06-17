# Gerenciar Convites, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/evento/<id>/convites/` | — | HTML | 200, 404 |
| POST | `/dashboard/evento/<id>/convites/` | ConviteForm | Redirect | 302, 200 |

1. Busca evento com validação de organizador 🟢 (`views.py:266`)
2. Stats: pendentes, respondidos, confirmados, declinados 🟢 (`views.py:268-271`)
3. GET → lista convites + form 🟢 (`views.py:281-292`)
4. POST → cria convite via `ConviteForm` 🟢 (`views.py:273-280`)
5. Filtro client-side por status via JS 🟢 (template)
6. Exclusão via endpoint separado (`excluir_convite`)

## Dependências

- `ConviteForm` (apenas nome_destinatario)
- `Convite`, `Evento` models
- Bootstrap modals (criar + confirmar exclusão)
