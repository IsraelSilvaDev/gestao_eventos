# Home — Página Inicial do Convidado

## Visão Geral

Página pública de entrada do sistema onde o convidado insere o código de acesso do convite para acessar o formulário de RSVP.

## Responsabilidades

- Exibir formulário de busca por código de acesso
- Validar o código contra a base de convites
- Redirecionar para a página de RSVP em caso de sucesso
- Exibir mensagem de erro para códigos inválidos

## Regras de Negócio

- RB02: Um convite = uma resposta, mas a home apenas localiza o convite 🟢
- Código é case-insensitive (convertido para upper case na view) 🟢

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Exibir formulário com campo de código (max 8 chars) | Must | Campo texto com placeholder "ABC12345" |
| RF-02 | Buscar convite por código exato (case-insensitive) | Must | Código "abc12345" encontra convite "ABC12345" |
| RF-03 | Redirecionar para `/evento/<codigo>/` se encontrado | Must | Status 302 para URL do convite |
| RF-04 | Exibir mensagem de erro se código não existir | Must | Mensagem "Código de acesso inválido" via Django messages |
| RF-05 | Exibir detalhes do evento na página (nome, data, local) após encontrar | Could | Não implementado — código redireciona direto para RSVP |

## Requisitos Não Funcionais

| Tipo | Requisito inferido | Evidência no código | Confiança |
|------|--------------------|---------------------|-----------|
| Segurança | Sem proteção contra brute force | `eventos/views.py:14-27` | 🔴 |
| Usabilidade | Feedback imediato via messages framework | `eventos/views.py:23` | 🟢 |

## Critérios de Aceitação

```gherkin
Dado um convite com código "ABC12345"
Quando o convidado insere "ABC12345" no formulário
Então ele é redirecionado para /evento/ABC12345/

Dado um código "XYZ99999" que não existe
Quando o convidado insere no formulário
Então a página exibe "Código de acesso inválido"
```

## Prioridade (MoSCoW)

| Requisito | MoSCoW | Justificativa |
|-----------|--------|---------------|
| Buscar convite por código | Must | Porta de entrada do sistema |
| Validação de código inexistente | Must | UX essencial |
| Exibir detalhes do evento | Could | Não implementado — feature aspiracional para versão futura |

## Rastreabilidade de Código

| Arquivo | Função / Classe | Cobertura |
|---------|-----------------|-----------|
| `eventos/views.py:12-27` | `home_view` | 🟢 |
| `eventos/forms.py:4-11` | `CodigoAcessoForm` | 🟢 |
| `templates/home.html` | Template | 🟢 |
