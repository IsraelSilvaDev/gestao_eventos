# ADR-002: Dashboard com Chart.js e Cards Interativos

**Data:** 2026-05-04 (inferido do commit `7e90df5` — "cards adicionado")
**Status:** Aceito 🟢
**Confiança:** 🟡 INFERIDO (baseado em evidências do código e commit)

## Contexto

O dashboard inicial era uma tabela simples com estatísticas básicas. Era necessário oferecer visualizações mais ricas e interativas para o organizador acompanhar as confirmações.

## Decisão

Implementar dashboard com:
- **Chart.js 4.4.1** via CDN para gráficos (doughnut de status + barras por evento)
- **4 stat cards** com gradientes, ícones e animações (total convites, respondidos, pendentes, taxa)
- **Tabela de eventos** com busca textual, filtro por status, ordenação por coluna
- **Toasts** para feedback de ações (link copiado, erro)
- Botões de ação inline (ver, editar, copiar link, WhatsApp)

## Alternativas Consideradas

1. **Gráficos server-side (matplotlib/Pillow)** — Imagens estáticas, sem interatividade. Descartado.

2. **Google Charts** — Dependência externa, Terms of Service restritivos. Descartado.

3. **Gráficos CSS-only** — Limitado a barras simples, sem doughnut. Descartado.

4. **Chart.js** — Leve, open-source, fácil integração com Django templates. Escolhido.

## Consequências

- Positivas:
  - Visualização rica e interativa sem recarregar página
  - Componentes reutilizáveis (stat-cards, toasts)
  - CDN reduz tamanho do deploy
  - Feedback visual imediato para o organizador

- Negativas:
  - Dependência de CDN externo (sem internet = sem gráficos)
  - Dados inline no HTML (`{{ confirmados|default:0 }}`) — podem ficar pesados com muitos eventos
  - JavaScript misturado no template (manutenção mais difícil)
  - Sem fallback para quando JavaScript está desabilitado

## Arquivos Afetados

- `templates/dashboard/dashboard.html` — Gráficos, cards, tabela, toasts
- `templates/dashboard/gerenciar_convites.html` — Stats, filtros, modais
- `templates/dashboard/detalhe_evento.html` — Cards de resumo
- `templates/responder_evento.html` — Animações de banner
