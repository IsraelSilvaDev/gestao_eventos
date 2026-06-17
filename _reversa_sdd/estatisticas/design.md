# Estatísticas, Design Técnico

| Método | Caminho | Saída | Status |
|--------|---------|-------|--------|
| GET | `/dashboard/estatisticas/` | HTML | 200 |

1. Agregações globais (mesma lógica do dashboard) 🟢 (`views.py:155-160`)
2. Itera eventos do organizador, computa stats por evento 🟢 (`views.py:162-176`)
3. Renderiza tabela `dashboard/estatisticas.html` 🟢 (`views.py:178-186`)
