# Deploy Gestão de Eventos - PythonAnywhere

## Arquivos para upload

Faça upload destes arquivos/pastas para PythonAnywhere:

```
gestao_eventos/      # Pasta do projeto Django
templates/           # Templates HTML
media/               # Imagens/uploads
db.sqlite3          # Banco de dados (se já tem dados)
requirements.txt    # Dependências
manage.py           # Arquivo de gerenciamento
```

## Passo a Passo

### 1. Criar virtualenv
No Bash console:
```bash
mkvirtualenv --python=/usr/bin/python3.11 gestao_venv
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar Web App

Acesse a aba **Web** > **Add a new web app**:
- Escolha "Manual configuration"
- Escolha Python 3.11

### 4. Configurar WSGI

Edite o arquivo WSGI (link na seção Code):
```python
import os
import sys

# Seu username do PythonAnywhere
path = '/home/SEU_USUARIO'

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gestao_eventos.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. Executar migrações
```bash
python manage.py migrate
```

### 6. Criar superusuário
```bash
python manage.py createsuperuser
```
Siga as instruções para criar admin.

### 7. Configurar Static Files

Na seção **Static files** do Web tab:

| URL | Directory |
|-----|-----------|
| /static/ | /home/SEU_USUARIO/staticfiles |
| /media/ | /home/SEU_USUARIO/media |

### 8. Criar superusuário admin

```bash
python manage.py createsuperuser
```

---

## Problemas comuns

### Erro 500 - Internal Server Error

1. Check os logs em **Web > Logs**
2. Verifique se virtualenv está configurado corretamente
3. Execute `python manage.py check` no Bash

### STATIC_ROOT warning

Execute:
```bash
python manage.py collectstatic
```

### Database locked

O SQLite não funciona bem com múltiplas conexões. Para produção, considere migrar para PostgreSQL (disponível nos planos pagos).

---

## Após atualizar o código

```bash
# No Bash console
git pull  # ou faça upload dos arquivos

python manage.py migrate
python manage.py collectstatic
```

Depois vá na aba **Web** e clique em **Reload**