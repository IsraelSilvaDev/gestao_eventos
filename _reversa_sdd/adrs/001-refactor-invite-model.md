# ADR-001: Separação do Modelo de Convite

**Data:** 2026-05-04 (inferido do commit `421f936` — "novas funcionalidades")
**Status:** Aceito 🟢
**Confiança:** 🟡 INFERIDO (baseado em evidências do código e migrações)

## Contexto

Originalmente, o modelo `Evento` possuía o campo `codigo_acesso` e `Resposta` tinha uma FK direta para `Evento`. Isso significava que cada evento tinha um único código de acesso compartilhado por todos os convidados, impossibilitando convites individuais com códigos únicos.

## Decisão

Criar o modelo `Convite` com:
- FK para `Evento`
- `codigo_acesso` único (gerado via UUID)
- `nome_destinatario` opcional

E alterar `Resposta` de FK(Evento) para OneToOneField(Convite).

## Alternativas Consideradas

1. **Manter código no Evento** — Cada evento teria um código único, mas não haveria rastreabilidade individual de convites. Descartado por limitar o controle do organizador.

2. **Usar slug em vez de UUID** — Mais legível, mas sem garantia de unicidade sem verificação extra. UUID foi escolhido por simplicidade.

3. **Convite como modelo abstrato** — Manter dados no Evento com herança. Descartado por adicionar complexidade desnecessária.

## Consequências

- Positivas:
  - Cada convidado tem código único → rastreabilidade individual
  - Organizador pode criar N convites por evento
  - Possibilidade de nomear destinatários opcionalmente
  - Base para funcionalidades futuras (notificações por convite, confirmação individual)

- Negativas:
  - Quebra de compatibilidade com dados existentes (migration 0003)
  - Perda do histórico de respostas anteriores (relacionamento mudou de FK para O2O)
  - Complexidade adicional na view de RSVP (agora precisa buscar Convite, não Evento)

## Arquivos Afetados

- `eventos/models.py` — Adicionado Convite, Acompanhante; alterado Resposta.convite para O2O
- `eventos/views.py` — Adaptado fluxo de RSVP para usar Convite
- `eventos/forms.py` — Adicionados ConviteForm, ConviteMultiploForm
- `eventos/admin.py` — Registrados ConviteAdmin, AcompanhanteInline
- `eventos/urls.py` — Rotas para gerenciamento de convites
- `eventos/migrations/0003_*.py` — Migration de refatoração
