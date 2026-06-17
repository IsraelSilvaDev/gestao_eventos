# Matriz de Impacto — Spec Impact Matrix

## Componentes vs. Artefatos

| Componente | Modelo | View | Form | Template | URL | Admin |
|-----------|--------|------|------|----------|-----|-------|
| **Evento** | Evento | criar_evento_view, editar_evento_view, dashboard_view, detalhe_evento_dashboard_view | EventoForm | form_evento.html, dashboard.html, detalhe_evento.html | /dashboard/criar/, /dashboard/evento/\<id\>/editar/ | EventoAdmin |
| **Convite** | Convite | gerenciar_convites_view, criar_convites_multiplos_view, excluir_convite_view, gerar_link_convite_view | ConviteForm, ConviteMultiploForm | gerenciar_convites.html, criar_convites_multiplos.html | /dashboard/evento/\<id\>/convites/, /dashboard/convite/\<id\>/excluir\|link/ | ConviteAdmin |
| **Resposta** | Resposta | responder_evento_view, dashboard_view, detalhe_evento_dashboard_view | RespostaForm | responder_evento.html, detalhe_evento.html | /evento/\<codigo\>/, /dashboard/evento/\<id\>/ | RespostaAdmin |
| **Acompanhante** | Acompanhante | responder_evento_view | — (inline) | responder_evento.html (JS dinâmico) | (inline na resposta) | AcompanhanteInline |
| **Autenticação** | User | LoginView, LogoutView, is_organizador | — | login.html, base.html | /login/, /logout/ | — |
| **Dashboard** | — | dashboard_view, estatisticas_dashboard_view | — | dashboard.html, estatisticas.html, admin/estatisticas.html, admin/index.html | /dashboard/, /dashboard/estatisticas/ | — |

## Matriz de Dependências entre Componentes

| Componente | Depende de | É dependido por |
|-----------|-----------|----------------|
| Evento | User | Convite |
| Convite | Evento | Resposta, Link |
| Resposta | Convite | Acompanhante |
| Acompanhante | Resposta | — |
| Autenticação | User | Todos os dashboards |
| Dashboard | Evento, Convite, Resposta | — |

## Endpoints vs. Componentes (Organização escolhida: endpoint)

| Endpoint | Componentes envolvidos |
|----------|----------------------|
| `/` | CodigoAcessoForm → Convite |
| `/evento/<codigo>/` | Convite, RespostaForm, Resposta, Acompanhante |
| `/sucesso/` | (estático) |
| `/login/` | User, LoginView |
| `/logout/` | User, LogoutView |
| `/dashboard/` | Evento, Convite, Resposta, User |
| `/dashboard/estatisticas/` | Evento, Convite, Resposta |
| `/dashboard/criar/` | EventoForm, Evento |
| `/dashboard/evento/<id>/` | Evento, Convite, Resposta, Acompanhante |
| `/dashboard/evento/<id>/editar/` | EventoForm, Evento |
| `/dashboard/evento/<id>/convites/` | Evento, ConviteForm, Convite |
| `/dashboard/evento/<id>/convites/criar/` | ConviteMultiploForm, Convite |
| `/dashboard/convite/<id>/excluir/` | Convite |
| `/dashboard/convite/<id>/link/` | Convite |

## Regras de Negócio vs. Componentes

| Regra | Componente |
|-------|-----------|
| RB01 — Geração UUID | Convite (models.py) |
| RB02 — Uma resposta por convite | Resposta (models.py, O2O) |
| RB03 — Validação status × pessoas | RespostaForm (forms.py, clean) |
| RB04 — Acompanhantes destrutivos | responder_evento_view (views.py) |
| RB05 — Documento obrigatório | Acompanhante (models.py) + HTML required |
| RB06 — Staff como organizador | is_organizador (views.py) |
| RB07 — Limite 50 lote | ConviteMultiploForm (forms.py) |
| RB08 — Convite anônimo | Convite (models.py, nome_destinatario nullable) |
| RB09 — Desmarcar é deletar | responder_evento_view (views.py) |
