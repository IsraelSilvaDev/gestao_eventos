# Gerar Link do Convite

## Responsabilidades

- Retornar URL absoluta do convite em JSON (usado pelo JS para copiar link)

## Requisitos Funcionais

| ID | Requisito | Prioridade |
|----|-----------|-----------|
| RF-01 | Validar ownership do convite | Must |
| RF-02 | Retornar JSON com link absoluto | Must |
| RF-03 | Construir URL com `request.build_absolute_uri` | Must |

## Rastreabilidade

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:338-342` | `gerar_link_convite_view` | 🟢 |
