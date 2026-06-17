# Fluxograma: dashboard_view

**Arquivo:** `eventos/views.py:110-149` 🟢 CONFIRMADO

## Comportamento

Calcula estatísticas globais e por evento, alimenta Chart.js no frontend.

```mermaid
flowchart TD
    A[GET /dashboard/] --> B[Filtrar eventos do organizador]
    B --> C[Ordernar por data DESC]
    
    C --> D[Agg: total_convites = Convite.objects.count]
    D --> E[Agg: respondidos = Convite.filter resposta__isnull=False]
    E --> F[Agg: pendentes = Convite.filter resposta__isnull=True]
    F --> G[Agg: confirmados = Resposta.filter status=confirmado]
    G --> H[Agg: declinados = Resposta.filter status=declinado]
    
    H --> I{total_convites > 0?}
    I -->|Sim| J[taxa = round(respondidos/total * 100, 1)]
    I -->|Não| K[taxa = 0]
    
    J --> L
    K --> L
    
    L --> M[Para cada evento:]
    M --> N[Contar convites do evento]
    N --> O[Contar confirmados do evento]
    O --> P[Contar declinados do evento]
    P --> Q[Pegar codigo_acesso do first convite]
    Q --> M
    
    M --> R[Dados pro template:<br>eventos, totais, taxa]
    R --> S[Render dashboard/dashboard.html]
    S --> T[Chart.js:<br>doughnut + bar charts]
```

## Ponto de Atenção 🟡 INFERIDO

~~`convites.first().codigo_acesso` na linha 137 — assume que o evento tem pelo menos 1 convite.~~ ✅ RESOLVIDO — guarda `if convites.exists()` em `views.py:138`
