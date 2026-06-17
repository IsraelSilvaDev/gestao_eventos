# Responder Evento, Tarefas de Implementação

## Pré-requisitos

- [ ] Modelos `Convite`, `Resposta`, `Acompanhante` criados
- [ ] Template `base.html` com Bootstrap 5 e messages

## Tarefas

- [ ] T-01, Implementar GET com formulário vazio ou preenchido
  - Origem: `eventos/views.py:29-95`
  - Critério de pronto: Convite sem resposta → form vazio; com resposta → form preenchido + alerta
  - Confiança: 🟢

- [ ] T-02, Implementar criação de nova resposta
  - Origem: `eventos/views.py:61-77`
  - Critério de pronto: POST com dados válidos → cria Resposta + Acompanhantes → redirect sucesso
  - Confiança: 🟢

- [ ] T-03, Implementar atualização de resposta existente
  - Origem: `eventos/views.py:43-60`
  - Critério de pronto: POST em convite com resposta → atualiza dados + recria acompanhantes
  - Confiança: 🟢

- [ ] T-04, Implementar desmarcar presença
  - Origem: `eventos/views.py:35-41`
  - Critério de pronto: POST com `desmarcar` → exclui resposta + acompanhantes → redirect
  - Confiança: 🟢

- [ ] T-05, Implementar `RespostaForm` com validação clean()
  - Origem: `eventos/forms.py:13-53`
  - Critério de pronto: Declinado → total_pessoas=0; Confirmado + total<1 → erro
  - Confiança: 🟢

- [ ] T-06, Criar template com formulário, banner, modal e JS dinâmico
  - Origem: `templates/responder_evento.html`
  - Critério de pronto: Campos de acompanhantes aparecem/desaparecem conforme status e total_pessoas
  - Confiança: 🟢

- [ ] T-07, Implementar loop de criação de acompanhantes com validação de nome vazio
  - Origem: `eventos/views.py:50-58, 68-76`
  - Critério de pronto: Apenas acompanhantes com nome não vazio são criados
  - Confiança: 🟢

## Tarefas de Teste

- [ ] TT-01, Happy path: criar resposta com 2 acompanhantes
- [ ] TT-02, Atualizar resposta de confirmado para declinado
- [ ] TT-03, Desmarcar e verificar que convite voltou a pendente
- [ ] TT-04, Tentar criar resposta com total_pessoas=0 → erro de validação
- [ ] TT-05, Acessar código inexistente → 404

## Ordem Sugerida

1. T-05 (RespostaForm) primeiro, base para tudo
2. T-06 (template) para ter a UI
3. T-01 (GET) para exibir o form
4. T-02, T-03, T-04, T-07 em sequência (POST handlers)

## Lacunas Pendentes (🔴)

- Definir se deve usar transação atômica (`transaction.atomic`) para salvar resposta + acompanhantes
- Validar formato de documento (CPF/RG) ou manter como texto livre
