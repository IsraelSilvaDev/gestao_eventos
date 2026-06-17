# Análise de Código — Gestão de Eventos

## Visão Geral

Sistema Django de página única (`eventos`) para gestão de eventos com fluxo de RSVP online. Arquitetura monolítica com 4 modelos, 12 views, 5 formulários e 13 templates.

## Estrutura do Módulo `eventos`

### 1. Modelos (models.py)

**Modelo: Evento** 🟢 CONFIRMADO
- Representa um evento criado por um organizador
- FK para `auth.User` (organizador)
- Campos: nome, data, local, descricao (opcional), banner (imagem opcional)
- Sem soft delete ou campos de controle (criado_em, atualizado_em)

**Modelo: Convite** 🟢 CONFIRMADO
- Representa um convite individual vinculado a um evento
- FK para `Evento` com `related_name="convites"`
- `codigo_acesso` único de 8 caracteres (UUID hex[:8].upper()) — gerado automaticamente
- `nome_destinatario` opcional

**Modelo: Resposta** 🟢 CONFIRMADO
- OneToOneField para `Convite` — cada convite tem no máximo UMA resposta
- Status binário: 'confirmado' / 'declinado'
- `total_pessoas` (default 1) — inclui o convidado principal
- `data_resposta` com `auto_now=True` (atualizado a cada modificação)
- `observacoes` opcional

**Modelo: Acompanhante** 🟢 CONFIRMADO
- FK para `Resposta` com `related_name="acompanhantes"`
- Campos: nome_completo, documento (RG/CPF)
- Criado/recriado a cada atualização da resposta

### 2. Views (views.py)

**Views Públicas:**
| View | Métodos | Descrição |
|------|---------|-----------|
| `home_view` | GET, POST | Formulário de código de acesso |
| `responder_evento_view` | GET, POST | RSVP completo (criar/atualizar/desmarcar + acompanhantes) |
| `sucesso_view` | GET | Página de confirmação |

**Views Protegidas (staff):**
| View | Métodos | Descrição |
|------|---------|-----------|
| `dashboard_view` | GET | Dashboard global com Chart.js + estatísticas |
| `estatisticas_dashboard_view` | GET | Tabela de estatísticas por evento |
| `detalhe_evento_dashboard_view` | GET | Respostas de um evento específico |
| `criar_evento_view` | GET, POST | Criar novo evento |
| `editar_evento_view` | GET, POST | Editar evento |
| `gerenciar_convites_view` | GET, POST | Listar/criar convites individuais |
| `criar_convites_multiplos_view` | GET, POST | Criar 1-50 convites em lote |
| `excluir_convite_view` | POST | Excluir convite |
| `gerar_link_convite_view` | GET | JSON com link absoluto do convite |

### 3. Formulários (forms.py)

| Form | Modelo | Campos | Validação especial |
|------|--------|--------|-------------------|
| `CodigoAcessoForm` | — | codigo | max_length=8 |
| `RespostaForm` | Resposta | nome_principal, status, total_pessoas, observacoes | Se declinado → total_pessoas=0; se confirmado → >= 1 |
| `EventoForm` | Evento | nome, data, local, descricao, banner | Auto form-control CSS |
| `ConviteForm` | Convite | nome_destinatario | — |
| `ConviteMultiploForm` | — | quantidade (1-50), nome_base (opcional) | — |

### 4. Autenticação e Autorização

- Critério de organizador: `is_authenticated and is_staff` 🟢 CONFIRMADO
- Decoradores: `@login_required(login_url='login')` + `@user_passes_test(is_organizador)`
- Login via `auth_views.LoginView` com template customizado
- Logout via `auth_views.LogoutView` (POST apenas)
- Não há registro público de organizadores

## Algoritmos e Lógica de Negócio

### 5.1 Geração de Código de Acesso 🟢 CONFIRMADO
```python
def gerar_codigo_acesso():
    return uuid.uuid4().hex[:8].upper()
```
Gera UUID v4, pega os primeiros 8 caracteres hex, converte para maiúsculas.
Colisão possível mas extremamente improvável (16^8 = 4.3 bilhões de combinações).

### 5.2 Validação de Resposta (RespostaForm.clean) 🟢 CONFIRMADO
- Se status == 'declinado' → `total_pessoas = 0` (forçado)
- Se status == 'confirmado' e `total_pessoas < 1` → ValidationError
- Regra de negócio: quem declina não leva acompanhantes

### 5.3 Processamento de Acompanhantes (responder_evento_view) 🟢 CONFIRMADO
- Acompanhantes são sempre deletados e recriados na atualização
- Campos dinâmicos: `acompanhante_nome[]` e `acompanhante_doc[]`
- Itens com nome vazio são ignorados

### 5.4 Dashboard — Estatísticas Agregadas 🟢 CONFIRMADO
- `Convite.objects.count()` — total global
- `Convite.objects.filter(resposta__isnull=False).count()` — respondidos
- `Convite.objects.filter(resposta__isnull=True).count()` — pendentes
- `Resposta.objects.filter(status='confirmado').count()` — confirmados
- `Resposta.objects.filter(status='declinado').count()` — declinados
- Taxa de resposta: `(respondidos / total) * 100` com 1 casa decimal

### 5.5 Dashboard — Dados por Evento 🟢 CONFIRMADO
- Itera sobre eventos do organizador
- Para cada evento: conta convites, confirmados, declinados via filtros de related_name
- Usa `convites.first().codigo_acesso` para o link → potencialmente frágil (assume que existe ao menos 1 convite)

### 5.6 Criação Múltipla de Convites 🟢 CONFIRMADO
- Recebe `quantidade` (1-50) e `nome_base` opcional
- Para i in range(quantidade): cria Convite com nome `{nome_base} {i+1}` ou só `nome_base` se qtdade==1
- Retorna mensagem de sucesso com contagem

### 5.7 Exclusão de Convite 🟢 CONFIRMADO
- Busca Convite por ID validando `evento__organizador=request.user`
- Exclui e redireciona para gerenciamento de convites

## Fluxos de Controle Complexos

### responder_evento_view
```
GET:
  ├── Convite existe? → 404 se não
  ├── Já tem resposta?
  │   ├── Sim: form preenchido + acompanhantes existentes + flag ja_respondeu
  │   └── Não: form vazio + lista vazia
POST:
  ├── 'desmarcar' in request.POST?
  │   ├── Sim: deleta acompanhantes → deleta resposta → redirect
  │   └── Não:
  │       ├── Já tem resposta?
  │       │   ├── Sim: form(instance=resposta) → se válido: atualiza, deleta+recria acompanhantes
  │       │   └── Não: form() → se válido: save(commit=False), associa convite, cria acompanhantes
```

### dashboard_view
```
├── Query eventos do organizador (ordenados por data DESC)
├── Agregações globais (total, respondidos, pendentes, confirmados, declinados)
├── Calcula taxa de resposta (round 1 decimal)
├── Para cada evento:
│   ├── Conta convites
│   ├── Conta confirmados
│   ├── Conta declinados
│   └── Pega primeiro codigo_acesso
└── Renderiza template com Chart.js
```

## Observações e Alertas 🟡 INFERIDO

1. **`convites.first().codigo_acesso`** no dashboard_view: assume que o evento tem ao menos 1 convite. Se o evento for recém-criado sem convites, causará AttributeError.
2. **Sem testes**: tests.py está vazio (apenas placeholder).
3. **Debug ativo**: `DEBUG = True` em settings.py — inseguro para produção.
4. **Secret key hardcoded**: fallback em settings.py, mas .env tem a chave real.
5. **Logout via POST apenas**: correto por segurança, mas pode confundir usuários sem JavaScript.
6. **Sem proteção contra brute force**: não há rate limiting na busca por código de acesso.
