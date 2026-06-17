# Criar Convites Múltiplos — Criação em Lote

## Responsabilidades

- Criar de 1 a 50 convites de uma só vez
- Gerar nomes sequenciais automaticamente (ex: "Convidado 1", "Convidado 2")

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Formulário com quantidade (1-50) e nome_base opcional | Must |
| RF-02 | Criar N convites com código único cada | Must |
| RF-03 | Nomear sequencialmente: `{nome_base} {i+1}` | Must |
| RF-04 | Redirecionar para gerenciamento de convites após criação | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:296-325` | `criar_convites_multiplos_view` | 🟢 |
| `eventos/forms.py:95-116` | `ConviteMultiploForm` | 🟢 |
