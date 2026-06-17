# Gerar Link do Convite, Design Técnico

| Método | Caminho | Entrada | Saída | Status |
|--------|---------|---------|-------|--------|
| GET | `/dashboard/convite/<id>/link/` | — | JSON | 200, 404 |

Resposta: `{"link": "http://domain.com/evento/ABC12345/"}`

1. Busca `Convite(id=id, evento__organizador=request.user)` 🟢 (`views.py:341`)
2. Retorna `JsonResponse({'link': build_absolute_uri(f'/evento/{convite.codigo_acesso}/')})` 🟢 (`views.py:342`)
