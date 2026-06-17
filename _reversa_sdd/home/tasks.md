# Home, Tarefas de Implementação

## Pré-requisitos

- [ ] Modelo `Convite` com campo `codigo_acesso` unique
- [ ] Template base `base.html` com Bootstrap e messages

## Tarefas

- [ ] T-01, Criar `CodigoAcessoForm` com campo CharField(max_length=8)
  - Origem no legado: `eventos/forms.py:4-11`
  - Critério de pronto: Form renderiza input com placeholder "ABC12345"
  - Confiança: 🟢

- [ ] T-02, Implementar `home_view` com GET (form vazio) e POST (validação)
  - Origem no legado: `eventos/views.py:12-27`
  - Critério de pronto: GET retorna 200 com form; POST válido redireciona; POST inválido mostra erro
  - Confiança: 🟢

- [ ] T-03, Buscar convite por código com uppercase
  - Origem no legado: `eventos/views.py:18-21`
  - Critério de pronto: Código "abc" encontra convite "ABC"
  - Confiança: 🟢

- [ ] T-04, Exibir mensagem de erro via messages framework
  - Origem no legado: `eventos/views.py:23`
  - Critério de pronto: código inválido exibe alerta Bootstrap no template
  - Confiança: 🟢

- [ ] T-05, Criar template `home.html` com form centralizado
  - Origem no legado: `templates/home.html`
  - Critério de pronto: Página com campo de código e botão "Confirmar Presença"
  - Confiança: 🟢

## Tarefas de Teste

- [ ] TT-01, Happy path: código válido → redirect para RSVP
- [ ] TT-02, Código inválido → mensagem de erro na mesma página
- [ ] TT-03, Código vazio → erro de validação do form
- [ ] TT-04, Código com caracteres especiais → aceito normalmente (UUID hex só tem 0-9, A-F)

## Ordem Sugerida

1. T-05 (template) primeiro, pois o form e a view dependem dele para renderizar
2. T-01 (form), T-02 (view), T-03 (busca), T-04 (mensagens) em sequência

## Lacunas Pendentes (🔴)

- Definir política de rate limiting para tentativas de código
- Decidir se código deve ser case-sensitive ou case-insensitive (atual: insensitive via .upper())
