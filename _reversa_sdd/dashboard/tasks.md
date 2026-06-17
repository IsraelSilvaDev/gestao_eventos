# Dashboard, Tarefas

- [ ] T-01, Implementar `dashboard_view` com agregações globais e por evento
  - Origem: `eventos/views.py:108-149`
  - Critério de pronto: View retorna stats corretas no context
  - Confiança: 🟢

- [ ] T-02, Criar template com 4 stat cards + animação
  - Origem: `templates/dashboard/dashboard.html:14-58`
  - Confiança: 🟢

- [ ] T-03, Implementar gráfico doughnut (Chart.js)
  - Origem: `templates/dashboard/dashboard.html:167-199`
  - Confiança: 🟢

- [ ] T-04, Implementar gráfico de barras (Chart.js)
  - Origem: `templates/dashboard/dashboard.html:201-246`
  - Confiança: 🟢

- [ ] T-05, Implementar tabela com busca, filtro e ordenação
  - Origem: `templates/dashboard/dashboard.html:96-148 + JS`
  - Confiança: 🟢

- [ ] T-06, Implementar funções copyLink e sendWhatsapp
  - Origem: `templates/dashboard/dashboard.html:406-436`
  - Confiança: 🟢

- [ ] T-07, Corrigir vulnerabilidade: `convites.first()` sem checagem
  - Origem: `eventos/views.py:137`
  - Critério de pronto: Evento sem convites não quebra a página
  - Confiança: 🔴

- [ ] T-08, Implementar fallback offline para CDN
  - Origem: `templates/dashboard/dashboard.html:156`
  - Confiança: 🟡
