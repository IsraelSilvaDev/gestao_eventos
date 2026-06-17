# Diagrama C4 — Containers (Nível 2)

```mermaid
C4Container
    title Diagrama de Containers - Gestão de Eventos

    Person(convidado, "Convidado", "Usuário com código de acesso")
    Person(organizador, "Organizador", "Staff do sistema")

    System_Boundary(sistema, "Gestão de Eventos") {
        Container(web, "Aplicação Web", "Django 6.0.3 + Python", "Processa requisições HTTP, renderiza templates gerencia dados")
        Container(db, "Banco de Dados", "SQLite / PostgreSQL", "Armazena eventos, convites, respostas, acompanhantes e dados de autenticação")
        Container(static, "Arquivos Estáticos", "staticfiles/", "CSS/JS coletados do admin Django")
        Container(media, "Arquivos de Mídia", "media/", "Banners de eventos enviados por organizadores")
    }

    System_Ext(cdn, "CDN", "Bootstrap 5, Chart.js, Bootstrap Icons")
    System_Ext(dj_admin, "Django Admin", "/admin/")

    Rel(convidado, web, "HTTPS", "Formulário RSVP")
    Rel(organizador, web, "HTTPS", "Dashboard + gestão")
    Rel(web, db, "Django ORM", "Leitura e escrita")
    Rel(web, static, "Servir estáticos", "URL /static/")
    Rel(web, media, "Servir mídia", "URL /media/")
    Rel(web, cdn, "Carregar assets", "CDN HTTPS")
    Rel(organizador, dj_admin, "HTTPS", "Admin avançado")
    Rel(dj_admin, db, "Django ORM", "Leitura e escrita")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```

## Containers

| Container | Tecnologia | Responsabilidade |
|-----------|-----------|------------------|
| **Web App** | Django 6.0.3 / Python | Processar requisições, autenticar, renderizar templates, servir formulários, gerar gráficos (dados inline) |
| **Banco de Dados** | SQLite / PostgreSQL | Persistir dados de Evento, Convite, Resposta, Acompanhante, auth.User |
| **Estáticos** | staticfiles/ | Arquivos coletados do admin Django |
| **Mídia** | media/ | Banners de eventos (imagens) |

## Observações

- **Sem container de cache** (Redis/Memcached) — todas as queries vão direto ao banco
- **Sem fila** (Celery/RQ) — operações síncronas
- **Sem API Gateway** — Django serve tudo diretamente
- **WSGI + Gunicorn** para produção (PythonAnywhere)
