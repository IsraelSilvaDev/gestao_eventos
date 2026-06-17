# Dicionário de Dados — Gestão de Eventos

## Modelo: Evento

| Campo | Tipo | Tabela | Obrigatório | Padrão | Descrição |
|-------|------|--------|-------------|--------|-----------|
| id | BigAutoField (PK) | eventos_evento | Sim | Auto | Identificador único |
| organizador | ForeignKey(User) | eventos_evento | Sim | — | FK para auth.User (criador do evento) |
| nome | CharField(200) | eventos_evento | Sim | — | Nome do evento |
| data | DateTimeField | eventos_evento | Sim | — | Data e hora do evento |
| local | CharField(300) | eventos_evento | Sim | — | Local do evento |
| descricao | TextField | eventos_evento | Não | null | Descrição detalhada |
| banner | ImageField | eventos_evento | Não | null | Banner promocional (upload_to='banners/%Y/%m/') |

🟢 CONFIRMADO

## Modelo: Convite

| Campo | Tipo | Tabela | Obrigatório | Padrão | Descrição |
|-------|------|--------|-------------|--------|-----------|
| id | BigAutoField (PK) | eventos_convite | Sim | Auto | Identificador único |
| evento | ForeignKey(Evento) | eventos_convite | Sim | — | FK para Evento (related_name='convites') |
| nome_destinatario | CharField(200) | eventos_convite | Não | null | Nome opcional do destinatário |
| codigo_acesso | CharField(8, unique) | eventos_convite | Sim | uuid4().hex[:8].upper() | Código único de 8 caracteres |

🟢 CONFIRMADO

## Modelo: Resposta

| Campo | Tipo | Tabela | Obrigatório | Padrão | Descrição |
|-------|------|--------|-------------|--------|-----------|
| id | BigAutoField (PK) | eventos_resposta | Sim | Auto | Identificador único |
| convite | OneToOneField(Convite) | eventos_resposta | Não | null | O2O para Convite (related_name='resposta') |
| nome_principal | CharField(200) | eventos_resposta | Sim | — | Nome do convidado principal |
| status | CharField(10) | eventos_resposta | Sim | — | 'confirmado' (Sim, irei) / 'declinado' (Não poderei ir) |
| total_pessoas | PositiveIntegerField | eventos_resposta | Sim | 1 | Total de pessoas (incluindo o convidado) |
| observacoes | TextField | eventos_resposta | Não | null | Observações (restrições, horário, etc.) |
| data_resposta | DateTimeField | eventos_resposta | Sim | auto_now | Data da resposta (atualiza na edição) |

🟢 CONFIRMADO

### Valores válidos de `status`

| Código | Display | Descrição |
|--------|---------|-----------|
| confirmado | Sim, irei | Convidado confirmou presença |
| declinado | Não poderei ir | Convidado recusou |

🟢 CONFIRMADO

## Modelo: Acompanhante

| Campo | Tipo | Tabela | Obrigatório | Padrão | Descrição |
|-------|------|--------|-------------|--------|-----------|
| id | BigAutoField (PK) | eventos_acompanhante | Sim | Auto | Identificador único |
| resposta | ForeignKey(Resposta) | eventos_acompanhante | Sim | — | FK para Resposta (related_name='acompanhantes') |
| nome_completo | CharField(200) | eventos_acompanhante | Sim | — | Nome completo do acompanhante |
| documento | CharField(50) | eventos_acompanhante | Sim | — | Documento (RG/CPF) |

🟢 CONFIRMADO

## Modelo: User (auth.User — Django built-in)

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| id | AutoField (PK) | Sim | Identificador único |
| username | CharField(150) | Sim | Nome de usuário |
| password | CharField(128) | Sim | Hash da senha |
| email | EmailField | Não | Email |
| first_name | CharField(150) | Não | Primeiro nome |
| last_name | CharField(150) | Não | Sobrenome |
| is_staff | BooleanField | Sim | Flag de staff (usada como organizador) |
| is_superuser | BooleanField | Sim | Flag de superusuário |
| is_active | BooleanField | Sim | Flag de conta ativa |
| date_joined | DateTimeField | Sim | Data de criação |

🟢 CONFIRMADO

## Relacionamentos (ER)

```
User 1──N Evento          (organizador)
Evento 1──N Convite       (convites)
Convite 1──1 Resposta     (resposta — OneToOne)
Resposta 1──N Acompanhante (acompanhantes)
```

🟢 CONFIRMADO

## Regras de Integridade

1. Um convite só pode ter UMA resposta (OneToOneField)
2. Excluir um Evento → cascade para Convites → Respostas → Acompanhantes
3. Excluir uma Resposta → cascade para Acompanhantes
4. `codigo_acesso` em Convite é UNIQUE
5. Ao declinar, `total_pessoas` é forçado para 0 (regra de negócio no form)
6. `data_resposta` atualiza automaticamente via `auto_now`

🟢 CONFIRMADO
