# Detalhe Evento, Design Técnico

| Método | Caminho | Saída | Status |
|--------|---------|-------|--------|
| GET | `/dashboard/evento/<id>/` | HTML | 200, 404 |

1. Busca `Evento(id=id, organizador=request.user)` ou 404 🟢 (`views.py:193`)
2. Busca `Resposta.objects.filter(convite__in=convites).order_by('-data_resposta')` 🟢 (`views.py:196`)
3. Agrega: `Sum('total_pessoas')` para confirmados 🟢 (`views.py:198-200`)
4. Conta: confirmados, declinados, pendentes 🟢 (`views.py:202-211`)

## Dependências

- `Evento`, `Convite`, `Resposta` models
- `is_organizador` check
