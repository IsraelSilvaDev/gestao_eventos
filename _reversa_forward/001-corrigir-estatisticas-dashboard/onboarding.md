# Onboarding — Como Testar a Correção

## Pré-requisitos

- Servidor de desenvolvimento rodando (`python manage.py runserver`)
- Pelo menos 2 usuários staff (organizadores) com eventos criados
- Pelo menos 1 convite por evento

## Passo a Passo

### 1. Preparar dados de teste

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from eventos.models import Evento, Convite, Resposta

# Criar organizador A
org_a = User.objects.create_user(username='org_a', password='teste123', is_staff=True)

# Criar organizador B
org_b = User.objects.create_user(username='org_b', password='teste123', is_staff=True)

# Criar evento para A
evento_a = Evento.objects.create(nome='Evento do A', data='2026-07-01 20:00', organizador=org_a)
convite_a = Convite.objects.create(evento=evento_a, nome_convidado='Convidado A1')
Convite.objects.create(evento=evento_a, nome_convidado='Convidado A2')

# Criar evento para B
evento_b = Evento.objects.create(nome='Evento do B', data='2026-07-15 20:00', organizador=org_b)
Convite.objects.create(evento=evento_b, nome_convidado='Convidado B1')
Convite.objects.create(evento=evento_b, nome_convidado='Convidado B2')
Convite.objects.create(evento=evento_b, nome_convidado='Convidado B3')
```

### 2. Verificar o bug (antes da correção)

1. Faça login como `org_a` e acesse `/dashboard/`
2. Anote o valor de "Total Convites" (deve mostrar 5 — todos do sistema)
3. O correto seria 2 (apenas os eventos de A)

### 3. Aplicar a correção

Editar `eventos/views.py` conforme o roadmap.

### 4. Verificar a correção

1. Refresh `/dashboard/` como `org_a`
2. "Total Convites" deve mostrar 2 (apenas eventos de A)
3. Faça login como `org_b`
4. "Total Convites" deve mostrar 3 (apenas eventos de B)

### 5. Verificar per-event stats

Os números de cada linha na tabela de eventos não devem mudar — continuam corretos.

### 6. Verificar página de estatísticas

Acessar `/dashboard/estatisticas/` com cada organizador e confirmar o filtro.

### 7. Rollback (se necessário)

```bash
git checkout eventos/views.py
```
