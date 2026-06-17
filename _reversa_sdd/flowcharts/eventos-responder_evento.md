# Fluxograma: responder_evento_view

**Arquivo:** `eventos/views.py:29-95` 🟢 CONFIRMADO

## Comportamento

Função com 3 modos de operação (criar, atualizar, desmarcar) + gerenciamento dinâmico de acompanhantes.

```mermaid
flowchart TD
    INICIO["GET /evento/&lt;codigo&gt;/"] --> GET_FLOW
    INICIO2["POST /evento/&lt;codigo&gt;/"] --> POST_FLOW
    
    subgraph GET_FLOW [GET - Exibir formulário]
        A[Buscar Convite por codigo_acesso] --> B{Found?}
        B -->|404| ERR[404 Not Found]
        B -->|OK| C{hasattr convite.resposta?}
        C -->|Sim| D[RespostaForm preenchido<br>+ lista acompanhantes<br>+ ja_respondeu=True]
        C -->|Não| E[RespostaForm vazio<br>+ lista vazia<br>+ ja_respondeu=False]
        D --> F[Render responder_evento.html]
        E --> F
    end
    
    subgraph POST_FLOW [POST - Processar resposta]
        G[Buscar Convite por codigo_acesso] --> H{ 'desmarcar' in POST? }
        
        H -->|Sim - Cancelar| I{hasattr resposta?}
        I -->|Sim| J[Deleta todos Acompanhantes]
        J --> K[Deleta Resposta]
        K --> L[Message: 'confirmacao desmarcada']
        I -->|Não| L
        L --> M[Redirect: responder_evento]
        
        H -->|Não - Salvar| N{hasattr resposta?}
        
        N -->|Sim - Atualizar| O[RespostaForm instance=resposta]
        O --> P{Form válido?}
        P -->|Não| F
        P -->|Sim| Q[form.save]
        Q --> R[Deleta todos Acompanhantes]
        R --> S[Percorre POST lists<br>acompanhante_nome[]<br>acompanhante_doc[]]
        S --> T[Para cada nome não vazio:<br>Acompanhante.objects.create]
        T --> U[Message: 'atualizada']
        
        N -->|Não - Criar| V[RespostaForm]
        V --> W{Form válido?}
        W -->|Não| F
        W -->|Sim| X[form.save commit=False]
        X --> Y[Associa response.convite = convite]
        Y --> Z[response.save]
        Z --> AA[Percorre POST lists<br>acompanhante_nome[]<br>acompanhante_doc[]]
        AA --> AB[Para cada nome não vazio:<br>Acompanhante.objects.create]
        AB --> U
        
        U --> AC[Redirect: sucesso]
    end
```

## Pontos de Atenção 🟡 INFERIDO

1. Acompanhantes são sempre deletados e recriados (abordagem destrutiva) — pode perder dados se houver falha entre o delete e o recreate
2. Não há validação de que o número de acompanhantes informado corresponde ao `total_pessoas - 1`
3. Não há transação atômica — se a criação de acompanhantes falhar, a resposta já foi salva
