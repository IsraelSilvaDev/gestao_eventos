# Criar Evento, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/criar/` | — | HTML | 200 |
| POST | `/dashboard/criar/` | EventoForm + FILES | Redirect | 302, 200 (erro) |

1. GET: Renderiza `EventoForm()` vazio 🟢 (`views.py:235-236`)
2. POST: Instancia `EventoForm(request.POST, request.FILES)` 🟢 (`views.py:224`)
3. Válido? → `form.save(commit=False)` → `evento.organizador = request.user` → `evento.save()` 🟢 (`views.py:227-230`)
4. Messages sucesso + redirect dashboard 🟢 (`views.py:232-233`)

## Dependências

- `EventoForm` (auto form-control CSS)
- `Evento` model
- `is_organizador` (staff check)
