# Diagrama C4 — Contexto (Nível 1)

## Sistema: Gestão de Eventos

```mermaid
C4Context
    title Diagrama de Contexto - Gestão de Eventos

    Person(convidado, "Convidado", "Pessoa que recebeu um código de convite para confirmar presença")
    Person(organizador, "Organizador (Staff)", "Usuário staff que cria e gerencia eventos, convites e respostas")
    Person(superadmin, "Superusuário", "Administrador do sistema com acesso ao Django Admin")

    System_Boundary(sistema, "Gestão de Eventos") {
        System(webapp, "Aplicação Web", "Django 6.0.3 — gerencia eventos, convites, RSVP e dashboard")
    }

    System_Ext(whatsapp, "WhatsApp Web", "Organizador compartilha links manualmente")
    System_Ext(cdn_bs, "Bootstrap CDN", "jsdelivr.net — CSS e JS de interface")
    System_Ext(cdn_chart, "Chart.js CDN", "cdn.jsdelivr.net — gráficos do dashboard")
    System_Ext(bs_icons, "Bootstrap Icons CDN", "cdn.jsdelivr.net — ícones da interface")
    System_Ext(dj_admin, "Django Admin Interface", "/admin/ — gestão avançada de dados")

    Rel(convidado, webapp, "Acessa formulário RSVP via código", "HTTPS")
    Rel(organizador, webapp, "Gerencia eventos, convites e estatísticas", "HTTPS")
    Rel(organizador, dj_admin, "Administração avançada", "HTTPS")
    Rel(superadmin, dj_admin, "Administração total", "HTTPS")
    Rel(webapp, cdn_bs, "Carrega Bootstrap", "CDN HTTPS")
    Rel(webapp, cdn_chart, "Carrega Chart.js", "CDN HTTPS")
    Rel(webapp, bs_icons, "Carrega ícones", "CDN HTTPS")
    Rel(organizador, whatsapp, "Compartilha links de convite", "HTTPS (manual)")

    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

## Usuários do Sistema

| Ator | Descrição | Acessa |
|------|-----------|--------|
| Convidado | Pessoa com código de convite | Apenas `/` e `/evento/<codigo>/` |
| Organizador | Staff Django | Dashboard, admin básico |
| Superusuário | is_superuser | Tudo, incluindo Django Admin completo |

## Sistemas Externos

| Sistema | Tipo | Direção | Descrição |
|---------|------|---------|-----------|
| WhatsApp Web | Manual | Saída | Organizador copia link e cola no WhatsApp |
| Bootstrap CDN | CDN | Entrada | Framework CSS/JS para frontend |
| Chart.js CDN | CDN | Entrada | Biblioteca de gráficos |
| Bootstrap Icons CDN | CDN | Entrada | Pacote de ícones |
| Django Admin | Built-in | Interno | Interface administrativa nativa do Django |
