# Dependências — Gestão de Eventos

## Produção

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| Django | 6.0.3 | Framework web |
| pillow | 12.2.0 | Processamento de imagens (banners) |
| asgiref | 3.11.1 | Interface ASGI do Django |
| sqlparse | 0.5.5 | Parser SQL (uso interno do Django) |

## Frontend (CDN)

| Biblioteca | Versão | Uso |
|------------|--------|-----|
| Bootstrap | 5.3.3 | CSS e JS de interface |
| Bootstrap Icons | 1.11.3 | Ícones |
| Chart.js | 4.4.1 | Gráficos do dashboard |

## Ambiente de Desenvolvimento

- Python 3.x
- SQLite (banco padrão)
- Virtualenv (venv/) para isolamento

## Deploy

O arquivo `.env` contém credenciais para PostgreSQL, mas o `settings.py` ainda usa SQLite por padrão.
Há suporte a deploy em PythonAnywhere documentado em `DEPLOY_PYTHONANYWHERE.md`.

## Scripts disponíveis (manage.py)

| Comando | Descrição |
|---------|-----------|
| `python manage.py runserver` | Servidor de desenvolvimento |
| `python manage.py migrate` | Aplicar migrações |
| `python manage.py makemigrations` | Criar migrações |
| `python manage.py collectstatic` | Coletar estáticos |
| `python manage.py createsuperuser` | Criar admin |
| `python manage.py test` | Rodar testes (vazio atualmente) |
