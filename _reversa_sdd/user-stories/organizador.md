# User Story: Fluxo do Organizador

## Jornada Completa

```mermaid
journey
    title Jornada do Organizador
    section Configuração
        Fazer login: 5: Organizador
        Criar evento: 4: Organizador
        Adicionar banner: 3: Organizador
    section Convites
        Criar convites individuais: 4: Organizador
        Criar convites em lote: 5: Organizador
        Copiar links para WhatsApp: 3: Organizador
    section Monitoramento
        Ver dashboard: 5: Organizador
        Analisar gráficos: 4: Organizador
        Ver detalhes do evento: 4: Organizador
        Filtrar convidados: 3: Organizador
    section Gerenciamento
        Editar evento: 4: Organizador
        Excluir convite: 3: Organizador
```

## Cenário 1: Organizador cria evento e convites

```gherkin
Dado que o organizador está logado no dashboard
Quando ele clica em "Novo Evento" e preenche nome, data, local
E adiciona um banner opcional
Então o evento é criado e aparece no dashboard

Quando ele acessa "Gerenciar Convites" do evento
E cria 10 convites em lote
Então 10 convites com códigos únicos são gerados
E o organizador pode copiar os links individualmente
```

## Cenário 2: Organizador analisa estatísticas

```gherkin
Dado que existem convites com respostas
Quando o organizador acessa o Dashboard
Então ele vê 4 stat cards com totais
E um gráfico doughnut com a distribuição
E uma tabela com todos os eventos e métricas
```
