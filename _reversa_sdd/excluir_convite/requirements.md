# Excluir Convite

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Validar ownership: convite deve pertencer a evento do organizador | Must |
| RF-02 | Excluir convite (cascade para resposta + acompanhantes) | Must |
| RF-03 | Redirecionar para gerenciamento de convites | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:328-335` | `excluir_convite_view` | 🟢 |
