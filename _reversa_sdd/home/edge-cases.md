# Home, Casos Extremos

| # | Caso | Comportamento esperado | Confiança |
|---|------|----------------------|-----------|
| 1 | Código com 9+ caracteres | Form rejeita (max_length=8) | 🟢 |
| 2 | Código com caracteres especiais (ex: "AB-C_12") | Form aceita (CharField sem validação extra), mas busca falha (UUID tem apenas 0-9, A-F) | 🟢 |
| 3 | Código com letras minúsculas | Convertido para uppercase na view | 🟢 |
| 4 | Código com espaços no início/fim | Django Form limpa via strip (padrão) | 🟡 |
| 5 | Dois convites com mesmo código | Impossível (constraint UNIQUE no banco) | 🟢 |
| 6 | Convite recém-excluído entre GET e POST | `Convite.DoesNotExist` → erro normal | 🟡 |
| 7 | Alta frequência de requisições | Sem proteção — vulnerável a brute force | 🔴 |
| 8 | Código XSS (ex: `<script>alert(1)</script>`) | Django escapa no template, seguro | 🟢 |
