# Dashboard, Design Técnico

| Método | Caminho | Saída | Status |
|--------|---------|-------|--------|
| GET | `/dashboard/` | HTML | 200 |

## Fluxo (Server)

1. Filtra `Evento.objects.filter(organizador=request.user)` ordenado por data DESC 🟢 (`views.py:112`)
2. Agregações globais: 🟢 (`views.py:114-119`)
   - `Convite.objects.count()` — total
   - `Convite.objects.filter(resposta__isnull=False)` — respondidos
   - `Resposta.objects.filter(status='confirmado')` — confirmados
3. Calcula taxa: `round(respondidos/total * 100, 1)` 🟢 (`views.py:122-123`)
4. Para cada evento: monta dict com id, nome, data, total_convites, confirmados, declinados, codigo 🟢 (`views.py:126-138`)

## Fluxo (Client — Chart.js)

1. Doughnut: labels `[Confirmados, Recusados, Pendentes]` com dados inline do template 🟢
2. Bar: labels = nomes dos eventos, data = total_convites 🟢

## Fluxo (Client — Interatividade)

1. Busca textual: filtra linhas por `textContent.includes(term)` 🟢
2. Filtro status: checa badges das linhas 🟢
3. Ordenação: sort client-side por coluna 🟢
4. Copiar link: cria textarea temporário, execCommand('copy') 🟢
5. WhatsApp: `https://wa.me/?text=` + encodeURI 🟢

## Dependências

- Chart.js 4.4.1 (CDN)
- Bootstrap 5
- `Evento`, `Convite`, `Resposta` models

## Riscos e Lacunas

- ~~🔴 **`convites.first().codigo_acesso`**: BUG — se evento não tiver convites, causa AttributeError~~ ✅ RESOLVIDO — guarda `if convites.exists()` adicionada em `eventos/views.py:138`
- 🟡 **Dados inline no HTML**: pode ficar pesado com dezenas de eventos
- 🟡 **CDN externo**: sem internet = sem gráficos
