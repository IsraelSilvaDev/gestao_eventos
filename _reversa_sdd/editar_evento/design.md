# Editar Evento, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/evento/<id>/editar/` | — | HTML | 200, 404 |
| POST | `/dashboard/evento/<id>/editar/` | EventoForm + FILES | Redirect | 302, 200 |

1. Busca `Evento(id=id, organizador=request.user)` ou 404 🟢 (`views.py:247`)
2. GET: `EventoForm(instance=evento)` 🟢 (`views.py:255`)
3. POST: `EventoForm(request.POST, request.FILES, instance=evento)` → save 🟢 (`views.py:249-251`)
4. Redirect para `detalhe_evento` 🟢 (`views.py:253`)
