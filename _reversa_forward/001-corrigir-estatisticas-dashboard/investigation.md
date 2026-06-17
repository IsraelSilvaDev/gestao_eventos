# Investigation — Filtro das Estatísticas Globais

## Pesquisa de Fundo

O bug foi identificado durante a revisão cruzada do Reversa (Fase 5). Ao analisar `eventos/views.py:110-149`, constatou-se que as queries de agregação global nas linhas 114-119 usam `Convite.objects.count()` e `Resposta.objects.filter()` sem qualquer filtro por organizador, enquanto o loop de per-event stats (linhas 126-138) já filtra corretamente via `evento.convites.all()`.

O problema também afeta `estatisticas_dashboard_view` (linhas 155-160), que replica a mesma lógica incorreta.

## Alternativas Avaliadas

### Alternativa A — Filtro via ORM com lookup de FK (escolhida)
Adicionar `.filter(evento__organizador=request.user)` nas queries afetadas.
- **Prós:** simples, uma linha por query, sem dependências novas
- **Contras:** join implícito entre 3 tabelas (Convite → Evento → User)
- **Custo:** ~2 minutos de edição

### Alternativa B — Subquery explícita com IDs
Obter IDs dos eventos do organizador primeiro, depois filtrar por `evento_id__in=eventos_ids`.
- **Prós:** mais explícito, sem join
- **Contras:** duas queries, mais código, sem ganho real de performance
- **Veredito:** over-engineering para este caso

### Alternativa C — View materializada no banco
Criar uma view no PostgreSQL que já filtra por organizador.
- **Prós:** performance em escala
- **Contras:** dependência de PostgreSQL, complexidade desnecessária para o volume atual
- **Veredito:** não se aplica

## Padrões Aplicáveis

- **Repository Pattern:** não se aplica (código não tem camada de repositório)
- **QuerySet reuse:** o filtro `Convite.objects.filter(evento__organizador=request.user)` poderia ser armazenado em variável para reuso dentro de cada view, mas as queries têm filtros adicionais diferentes (`resposta__isnull=False`, `status='confirmado'`, etc.)

## Referências

- `_reversa_sdd/dashboard/design.md#L7-L15` — descrição original com o bug
- `_reversa_sdd/domain.md#RB10` — regra inferida sobre isolamento
- `eventos/views.py:110-149` — código atual do dashboard
- `eventos/views.py:153-186` — código atual das estatísticas
