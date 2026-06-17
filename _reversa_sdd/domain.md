# Glossário e Regras de Domínio — Gestão de Eventos

## Glossário

| Termo | Definição |
|-------|-----------|
| **Evento** | Entidade que representa uma ocasião (festa, reunião, confraternização) criada por um organizador |
| **Organizador** | Usuário staff (`is_staff=True`) que cria e gerencia eventos, convites e respostas |
| **Convidado** | Pessoa que recebe um convite com código de acesso único |
| **Convite** | Registro individual vinculado a um evento, com código único de 8 caracteres |
| **Resposta (RSVP)** | Confirmação ou recusa do convidado a um convite |
| **Acompanhante** | Pessoa adicional que o convidado principal leva ao evento |
| **Código de Acesso** | Chave única alfanumérica de 8 caracteres que identifica um convite |
| **RSVP** | Répondez s'il vous plaît — confirmação de presença |

🟢 CONFIRMADO

## Regras de Negócio

### RB01 — Geração de Código de Acesso 🟢 CONFIRMADO
- Código é gerado automaticamente como `uuid.uuid4().hex[:8].upper()`
- É único por convite (constraint UNIQUE no banco)
- 8 caracteres hexadecimais maiúsculos → ~4.3 bilhões de combinações

### RB02 — Uma Resposta por Convite 🟢 CONFIRMADO
- Cada convite pode ter no máximo UMA resposta (OneToOneField)
- Se o convidado já respondeu e tenta novamente, o sistema atualiza a resposta existente

### RB03 — Validação de Pessoa por Status 🟢 CONFIRMADO
- Se o convidado **confirma** presença: `total_pessoas >= 1`
- Se o convidado **declina**: `total_pessoas` é forçado a 0
- Regra: quem não vai ao evento não pode levar acompanhantes

### RB04 — Gerenciamento Destrutivo de Acompanhantes 🟢 CONFIRMADO
- Ao atualizar uma resposta, TODOS os acompanhantes são deletados e recriados
- É uma abordagem "replace all" — não há diff ou atualização seletiva

### RB05 — Acompanhantes Exigem Documento 🟢 CONFIRMADO
- Cada acompanhante deve ter nome completo e documento (RG/CPF)
- Campos obrigatórios no frontend (HTML `required`)

### RB06 — Organizador Precisa Ser Staff 🟢 CONFIRMADO
- Critério: `user.is_authenticated and user.is_staff`
- Apenas `is_staff` pode acessar dashboard e gerenciar eventos
- Não há papel "organizador" separado do staff do Django

### RB07 — Limite de Criação em Lote 🟢 CONFIRMADO
- Máximo de 50 convites por vez na criação múltipla
- Mínimo de 1 convite

### RB08 — Convite Pode Ser Anônimo 🟢 CONFIRMADO
- `nome_destinatario` é opcional
- Convite pode existir sem destinatário nomeado

### RB09 — Desmarcar é Voltar ao Estado Pendente 🟢 CONFIRMADO
- Convidado pode desmarcar presença a qualquer momento
- Ação exclui a resposta e retorna o convite ao estado pendente
- Não há soft delete — a resposta é fisicamente removida

## Regras Implícitas (Inferidas)

### RB10 — Evento Precisa de ao Menos um Convite para Gerar Link 🟡 INFERIDO
- O dashboard pega `convites.first().codigo_acesso`
- Se evento recém-criado não tiver convites, o link do evento não estará disponível

### RB11 — Sem Confirmação por Lote 🟡 INFERIDO
- Não há funcionalidade para confirmar/declinar convites em massa
- Cada convidado responde individualmente via seu código único

### RB12 — Sem Notificações Automáticas 🟡 INFERIDO
- Não há envio automático de e-mail, SMS ou push
- O organizador compartilha links manualmente (WhatsApp, cópia de link)

### RB13 — Sem Controle de Vagas/Limite de Convidados 🟡 INFERIDO
- Evento não tem campo de capacidade máxima
- Não há validação de "evento lotado"

## Lacunas 🔴 (Prioridade: Correção — confirmado por Israel)

### L01 — Auditoria 🔴
- Não há log de quem criou/editou/excluiu convites
- `data_resposta` usa `auto_now` — perde o timestamp original após edição
- Prioridade: adicionar logging de operações CRUD

### L02 — Validação de Documento 🔴
- `documento` em Acompanhante é CharField(50) sem validação de formato
- Aceita qualquer string de até 50 caracteres
- Prioridade: adicionar validação de CPF/CNPJ no campo

### L03 — Privacidade de Dados 🔴
- Dados de convidados (nome, documento) não têm proteção especial
- Não há política de retenção ou exclusão programada
- Prioridade: adicionar anonimização ou expurgo programado

### L04 — Testes 🔴
- `tests.py` vazio — nenhuma cobertura de teste
- Plano: escrever testes para fluxos principais (RSVP, criação de evento, geração de convites)
