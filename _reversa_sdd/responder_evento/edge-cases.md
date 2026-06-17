# Responder Evento, Casos Extremos

| # | Caso | Comportamento esperado | Confiança |
|---|------|----------------------|-----------|
| 1 | total_pessoas = 1000 | Aceito (PositiveIntegerField sem上限) | 🟢 |
| 2 | 50 acompanhantes de uma vez | Todos criados (validação JS pode falhar, backend aceita) | 🟢 |
| 3 | Acompanhante com nome de 200+ chars | Truncado pelo CharField(200) no banco | 🟢 |
| 4 | Documento com caracteres especiais | Aceito (sem validação de formato) | 🟢 |
| 5 | Dois POSTs simultâneos | Race condition: um pode sobrescrever o outro, acompanhantes podem duplicar | 🔴 |
| 6 | Desmarcar sem resposta existente | Simplesmente redirect (hasattr falso) | 🟢 |
| 7 | Código de convite com caracteres inválidos | 404 (get_object_or_404) | 🟢 |
| 8 | Banner quebrado (imagem não encontrada) | Template exibe tag img com broken link, sem erro no servidor | 🟡 |
| 9 | Observações com HTML/script | Django escapa no template | 🟢 |
| 10 | Convidado recarrega página após desmarcar | Form vazio, pode criar nova resposta | 🟢 |
