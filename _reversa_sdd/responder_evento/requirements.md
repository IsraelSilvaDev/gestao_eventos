# Responder Evento — Formulário de RSVP

## Visão Geral

Endpoint principal para o convidado confirmar ou recusar presença em um evento. Suporta criação, atualização e cancelamento de resposta, com campos dinâmicos para acompanhantes.

## Responsabilidades

- Exibir detalhes do evento (nome, data, local, banner)
- Permitir que o convidado confirme ou decline presença
- Permitir atualização de resposta existente
- Permitir desmarcar (cancelar) a resposta
- Coletar dados de acompanhantes (nome + documento)

## Regras de Negócio

- RB02: Uma resposta por convite (OneToOneField) 🟢
- RB03: Confirmado → total_pessoas ≥ 1; Declinado → total_pessoas = 0 🟢
- RB04: Acompanhantes deletados e recriados a cada atualização 🟢
- RB05: Acompanhantes exigem nome e documento 🟢
- RB09: Desmarcar exclui a resposta, volta ao estado pendente 🟢

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Exibir detalhes do evento com banner | Must | Nome, data formatada, local, descrição e banner visíveis |
| RF-02 | Formulário com nome, status (radio), total_pessoas, observações | Must | Campos renderizados com labels corretos |
| RF-03 | Se já respondeu, pré-preenche form e exibe alerta | Must | Form com dados existentes + banner "Você já confirmou" |
| RF-04 | Se já respondeu, permitir desmarcar via modal | Must | Botão "Desmarcar" abre modal de confirmação |
| RF-05 | Desmarcar exclui resposta e acompanhantes | Must | POST com `desmarcar` → resposta deletada, redirect |
| RF-06 | Criar nova resposta com acompanhantes | Must | Salva resposta + N acompanhantes |
| RF-07 | Atualizar resposta (deleta + recria acompanhantes) | Must | Form pré-preenchido → atualiza resposta + recria acompanhantes |
| RF-08 | Campos dinâmicos de acompanhante baseados em total_pessoas | Should | JS cria/remove campos conforme total_pessoas - 1 |
| RF-09 | Exibir observações e botão de envio | Must | Campo textarea para observações, botão "Enviar" / "Atualizar" |

## Critérios de Aceitação

```gherkin
Dado um convite sem resposta
Quando o convidado preenche o formulário com status "confirmado" e 3 pessoas
Então uma resposta é criada com total_pessoas=3 e 2 acompanhantes

Dado uma resposta existente com status "confirmado"
Quando o convidado clica "Desmarcar" e confirma
Então a resposta é excluída e o convite volta ao estado pendente

Dado uma resposta existente
Quando o convidado atualiza de "confirmado" para "declinado"
Então total_pessoas passa a ser 0 e acompanhantes são removidos
```

## Rastreabilidade de Código

| Arquivo | Função / Classe | Cobertura |
|---------|-----------------|-----------|
| `eventos/views.py:29-95` | `responder_evento_view` | 🟢 |
| `eventos/forms.py:13-53` | `RespostaForm` | 🟢 |
| `templates/responder_evento.html` | Template | 🟢 |
