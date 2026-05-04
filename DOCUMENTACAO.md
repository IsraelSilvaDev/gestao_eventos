# Sistema de Gestão de Eventos - Documentação

## 📋 Visão Geral

Sistema web para gerenciamento de eventos com confirmação de presença (RSVP). Permite criar eventos, gerar convites, acompanhar respostas e visualizar estatísticas em tempo real.

---

## 🎯 Funcionalidades

### 1. Área Pública (Para Convidados)

#### 1.1 Página Inicial
- Campo para inserção do código de acesso do evento
- Validação do código e redirecionamento para o formulário de resposta

#### 1.2 Formulário de RSVP
- Nome completo do convidado principal
- Opção de resposta: "Sim, irei" ou "Não poderei ir"
- Número total de pessoas (incluindo o convidado)
- Observações (restrições alimentares, horário de chegada, etc.)
- Proteção contra respostas duplicadas (um convite = uma resposta)

#### 1.3 Página de Confirmação
- Mensagem de agradecimento após responder

---

### 2. Área do Organizador (Dashboard)

#### 2.1 Dashboard Principal
**URL:** `/dashboard/`

**Cards de Estatísticas:**
- Total de Convites enviados
- Convites Respondidos
- Convites Pendentes
- Taxa de Resposta (%)

**Gráficos Interativos (Chart.js):**
- Gráfico de rosca: Status das respostas (confirmados, recusados, pendentes)
- Gráfico de barras: Convites por evento

**Tabela de Eventos:**
- Nome do evento
- Data e hora
- Total de convites
- Confirmados
- Recusados
- Ações: Ver respostas, Editar, Copiar link

**Recursos:**
- Design responsivo para mobile
- Animações suaves
- Toasts de notificação
- Clique na linha para detalhar evento

#### 2.2 Criar Evento
**URL:** `/dashboard/criar/`

- Nome do evento
- Data e hora
- Local
- Descrição (opcional)

#### 2.3 Editar Evento
**URL:** `/dashboard/evento/<id>/editar/`

#### 2.4 Detalhes do Evento
**URL:** `/dashboard/evento/<id>/`

- Resumo: Total de pessoas confirmadas, confirmados, declinados
- Lista de respostas com detalhes
- Botão para gerenciar convites

#### 2.5 Gerenciar Convites
**URL:** `/dashboard/evento/<id>/convites/`

**Funcionalidades:**
- Criar convite individual com nome do destinatário
- Criar múltiplos convites (1-50 de uma vez)
- Lista de convites com:
  - Código único
  - Nome do destinatário
  - Status (Pendente/Respondido)
  - Resposta (Confirmado/Declinado)
- Ações por convite:
  - Copiar código
  - Copiar link completo
  - Visualizar página de resposta
  - Excluir convite (com confirmação)

---

### 3. Interface de Administração (Django Admin)

**URL:** `/admin/`

Modelos disponíveis:
- **Eventos** - Lista e cria eventos com convites inline
- **Convites** - Busca por código, evento ou destinatário
- **Respostas** - Lista respostas com acompanhantes inline
- **Acompanhantes** - Gerenciado via Resposta

---

## 🛠️ Tecnologias

- **Backend:** Django 5.x (Python 3.12)
- **Frontend:** HTML5, CSS3, JavaScript
- **Frameworks UI:** Bootstrap 5, Bootstrap Icons
- **Gráficos:** Chart.js
- **Banco de Dados:** SQLite (padrão) / PostgreSQL (produção)

---

## 📊 Modelos de Dados

### Evento
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | BigAutoField | PK |
| organizador | ForeignKey(User) | Criador do evento |
| nome | CharField(200) | Nome do evento |
| data | DateTimeField | Data e hora |
| local | CharField(300) | Localização |
| descricao | TextField | Descrição opcional |

### Convite
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | BigAutoField | PK |
| evento | ForeignKey(Evento) | Evento relacionado |
| nome_destinatario | CharField(200) | Nome do destinatário |
| codigo_acesso | CharField(8, unique) | Código único |

### Resposta
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | BigAutoField | PK |
| convite | OneToOneField(Convite) | Convite responded |
| nome_principal | CharField(200) | Nome do respondente |
| status | ChoiceField | confirmado/declinado |
| total_pessoas | PositiveIntegerField | Total de pessoas |
| observacoes | TextField | Observações |
| data_resposta | DateTimeField | Data da resposta |

### Acompanhante
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | BigAutoField | PK |
| resposta | ForeignKey(Resposta) | Resposta relacionada |
| nome_completo | CharField(200) | Nome do acompanhante |
| documento | CharField(50) | RG/CPF |

---

## 🚀 Como Executar

### 1. Ativar Virtual Environment
```bash
cd gestao_eventos
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2. Executar Migrações
```bash
python manage.py migrate
```

### 3. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 4. Iniciar Servidor
```bash
python manage.py runserver
```

### 5. Acessar
- **Dashboard:** http://localhost:8000/dashboard/
- **Admin Django:** http://localhost:8000/admin/
- **Página pública:** http://localhost:8000/

---

## 🔐 Fluxo de Uso

### Para o Organizador:
1. Acessar `/dashboard/` e fazer login
2. Criar um novo evento
3. Gerenciar convites (criar individuais ou em massa)
4. Copiar links dos convites para enviar aos convidados
5. Acompanhar estatísticas e respostas em tempo real

### Para o Convidado:
1. Receber link do convite pelo organizador
2. Acessar a página e inserir código (se necessário)
3. Preencher formulário de resposta
4. Ver página de confirmação

---

## 📝 Rotas Disponíveis

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial pública |
| `/evento/<codigo>/` | Formulário de resposta |
| `/sucesso/` | Página de confirmação |
| `/login/` | Login do organizador |
| `/logout/` | Logout |
| `/dashboard/` | Dashboard principal |
| `/dashboard/estatisticas/` | Estatísticas detalhadas |
| `/dashboard/criar/` | Criar novo evento |
| `/dashboard/evento/<id>/` | Detalhes do evento |
| `/dashboard/evento/<id>/editar/` | Editar evento |
| `/dashboard/evento/<id>/convites/` | Gerenciar convites |
| `/dashboard/evento/<id>/convites/criar/` | Criar múltiplos convites |
| `/admin/` | Interface admin Django |

---

## ⚙️ Configurações

### Variáveis de Ambiente
- `SECRET_KEY` - Chave secreta do Django
- `DEBUG` - Modo debug (True/False)
- `ALLOWED_HOSTS` - Hosts permitidos

###settings.py
O projeto está configurado com:
- Autenticação via Django.contrib.auth
- Session authentication
- Messages framework para feedback
- Static files e media files

---

## 🔧 Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Servidor de desenvolvimento
python manage.py runserver

# Shell Django
python manage.py shell
```

---

## 📄 Licença

Este projeto é para fins educacionais e de demonstração.

---

## 👤 Autor

Desenvolvido com Django Framework