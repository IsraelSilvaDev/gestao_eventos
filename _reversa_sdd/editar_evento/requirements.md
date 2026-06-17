# Editar Evento — Atualização de Dados

## Visão Geral

Formulário protegido para organizadores editarem eventos existentes.

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Apenas o organizador dono do evento pode editar | Must |
| RF-02 | Formulário pré-preenchido com dados atuais | Must |
| RF-03 | Upload de novo banner substitui o anterior | Should |
| RF-04 | Redirecionar para detalhe do evento após salvar | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:245-260` | `editar_evento_view` | 🟢 |
| `eventos/forms.py:55-79` | `EventoForm` | 🟢 |
