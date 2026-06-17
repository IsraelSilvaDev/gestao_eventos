# Matriz de Permissões — Gestão de Eventos

## Papéis

| Papel | Critério Django | Descrição |
|-------|-----------------|-----------|
| Convidado (anon) | `is_anonymous` ou `is_authenticated=False` | Acesso público apenas |
| Convidado (autenticado) | `is_authenticated=True` e `is_staff=False` | Acesso público + autenticação (não usado no sistema) |
| Organizador | `is_authenticated=True` e `is_staff=True` | Acesso completo ao dashboard do organizador |
| Superusuário | `is_superuser=True` | Acesso total (inclui admin Django) |

🟢 CONFIRMADO

## Matriz de Permissões

| Funcionalidade | Convidado (anon) | Convidado (auth) | Organizador | Superusuário |
|---------------|:----------------:|:----------------:|:-----------:|:------------:|
| **Página Inicial** (`/`) | ✅ | ✅ | ✅ | ✅ |
| **Formulário RSVP** (`/evento/<codigo>/`) | ✅ | ✅ | ✅ | ✅ |
| **Sucesso** (`/sucesso/`) | ✅ | ✅ | ✅ | ✅ |
| **Login** (`/login/`) | ✅ | ✅ | ✅ | ✅ |
| **Logout** (`/logout/`) | ❌ | ❌ | ✅ | ✅ |
| **Dashboard** (`/dashboard/`) | ❌ | ❌ | ✅ | ✅ |
| **Estatísticas** (`/dashboard/estatisticas/`) | ❌ | ❌ | ✅ | ✅ |
| **Criar Evento** (`/dashboard/criar/`) | ❌ | ❌ | ✅ | ✅ |
| **Editar Evento** (`/dashboard/evento/<id>/editar/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Detalhes Evento** (`/dashboard/evento/<id>/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Gerenciar Convites** (`/dashboard/evento/<id>/convites/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Criar Convites Lote** (`/dashboard/.../convites/criar/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Excluir Convite** (`/dashboard/convite/<id>/excluir/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Gerar Link Convite** (`/dashboard/convite/<id>/link/`) | ❌ | ❌ | ✅ (próprio) | ✅ |
| **Admin Django** (`/admin/`) | ❌ | ❌ | ❌ | ✅ |

## Observações sobre Ownership

### Evento
- Organizador só vê/edita/exclui eventos onde `evento.organizador == request.user`
- Verificação via `get_object_or_404(Evento, id=id, organizador=request.user)` 🟢 CONFIRMADO

### Convite
- Organizador só gerencia convites de seus próprios eventos
- Exclusão verifica `evento__organizador=request.user` 🟢 CONFIRMADO

### Resposta
- Respostas são visualizadas indiretamente via evento
- Convidado só interage com sua própria resposta via código de acesso (não há autenticação do convidado) 🟡 INFERIDO

## Lacunas 🔴

### L01 — Delegação de Acesso
- Não há como delegar gestão de um evento a outro organizador
- Apenas o criador do evento pode gerenciá-lo

### L02 — Registro de Organizadores
- Não há fluxo de registro de organizadores
- Criar organizador requer acesso ao admin Django ou shell

### L03 — Convidado não é um Usuário Real
- Convidados não têm conta no sistema
- Não é possível rastrear histórico de um convidado entre eventos
- Dados de acompanhantes não são reutilizáveis entre eventos

### L04 — Sem Permissões Granulares
- Não há níveis de organizador (editor, visualizador, admin de evento)
- Não há permissões por funcionalidade dentro do dashboard
