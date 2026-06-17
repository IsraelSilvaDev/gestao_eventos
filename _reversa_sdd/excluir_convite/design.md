# Excluir Convite, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/convite/<id>/excluir/` | — | Redirect | 302, 404 |

1. Busca `Convite(id=id, evento__organizador=request.user)` ou 404 🟢 (`views.py:331`)
2. `convite.delete()` — cascade para Resposta + Acompanhantes 🟢 (`views.py:333`)
3. Redirect para `gerenciar_convites` do evento 🟢 (`views.py:335`)
