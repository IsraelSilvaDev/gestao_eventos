# Criar Evento — Formulário de Criação

## Visão Geral

Formulário protegido para organizadores criarem novos eventos.

## Responsabilidades

- Exibir formulário de criação de evento
- Associar automaticamente o organizador logado
- Validar e salvar o evento
- Redirecionar para o dashboard

## Requisitos Funcionais

| ID | Requisito | Prioridade | Critério de Aceite |
|----|-----------|-----------|-------------------|
| RF-01 | Apenas staff pode acessar (login_required + user_passes_test) | Must | Redireciona para /login/ se não autenticado |
| RF-02 | Formulário com nome, data (datetime-local), local, descrição, banner | Must | Todos os campos renderizados |
| RF-03 | Associar organizador = request.user (commit=False) | Must | Evento salvo com organizador correto |
| RF-04 | Redirecionar para dashboard após criar | Must | 302 para /dashboard/ + mensagem sucesso |
| RF-05 | Upload de banner via ImageField | Should | Arquivo de imagem aceito e salvo em media/banners/ |

## Rastreabilidade de Código

| Arquivo | Função | Cobertura |
|---------|--------|-----------|
| `eventos/views.py:221-242` | `criar_evento_view` | 🟢 |
| `eventos/forms.py:55-79` | `EventoForm` | 🟢 |
| `templates/dashboard/form_evento.html` | Template | 🟢 |
