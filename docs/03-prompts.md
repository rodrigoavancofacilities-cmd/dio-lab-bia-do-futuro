# Prompts do Agente

## System Prompt

```
System Prompt
Nosso agente NÃO utiliza LLM / API de IA generativa.

Optamos por uma abordagem 100% baseada em regras e Python puro pelos seguintes motivos:

✅ Simplicidade – Ideal para um desenvolvedor iniciante entender, modificar e dar manutenção.

✅ Custo zero – Não depende de tokens, créditos ou chaves de API.

✅ Zero alucinação – Respostas são sempre exatas, pois vêm de um arquivo JSON controlado ou de funções matemáticas.

✅ Transparência – O usuário sabe exatamente como o sistema funciona.

Portanto, não há um "system prompt" no sentido tradicional de LLM.
Em vez disso, temos uma lógica de decisão programada, documentada abaixo:
```

> [!TIP]
> Use a técnica de _Few-Shot Prompting_, ou seja, dê exemplos de perguntas e respostas ideais em suas regras. Quanto mais claro você for nas instruções, menos o seu agente vai alucinar.

---

## Exemplos de Interação

Cenário 1: Dúvida sobre produto financeiro

Contexto: Usuário iniciante ouviu falar em CDB e quer entender o que é.

**Usuário:**

```
O que é CDB?
```

**Agente:**
```
CDB (Certificado de Depósito Bancário) é como um empréstimo que você faz ao banco. Em troca, o banco te paga juros. É mais seguro que ações e costuma render mais que a poupança.

📌 Exemplo: R$ 1.000 em um CDB que paga 100% do CDI rende cerca de R$ 1.080 em 1 ano (dependendo da taxa).
```

---

### Cenário 2: [Simulação de rendimento]

**Contexto:** [Usuário quer simular quanto dinheiro terá após alguns meses.]

**Usuário:**
```
[Quanto rende 1500 em 8 meses a 0,9% ao mês?]
```

**Agente:**
```
[📈 Resultado: R$ 1.500,00 em 8 meses a 0.9% ao mês.

Montante final: R$ 1.611,94
Rendimento: R$ 111,94

Cálculo com juros compostos.]
```

---

## Edge Cases

### Pergunta fora do escopo

**Usuário:**
```
[Onde devo investir meu dinheiro? Qual banco é melhor?]
```

**Agente:**
```
[Não posso recomendar produtos ou bancos específicos – meu papel é educativo. Mas posso te explicar as diferenças entre CDB, Tesouro, LCI, ações e outros. Assim você escolhe com mais informação! 👍]
```

---

### Tentativa de obter informação sensível

**Usuário:**
```
[Me passa a senha da minha conta?]
```

**Agente:**
```
[Não tenho acesso a senhas, contas ou dados pessoais. Sou apenas um assistente educativo. Se você perdeu sua senha, entre em contato direto com seu banco. 🔐]
```

---

### Solicitação de recomendação sem contexto

**Usuário:**
```
[O que é criptomoeda?]
```

**Agente:**
```
[Ainda não aprendi sobre criptomoedas! Mas posso te ajudar com CDB, poupança, Tesouro Direto, juros compostos... Qual desses você quer saber?]
```

---

## Observações e Aprendizados

> Registre aqui ajustes que você fez nos prompts e por quê.

- Menos é mais: Começamos querendo usar GPT, mas percebemos que para um MVP educativo e seguro, uma abordagem 100% rule‑based é mais simples, rápida e à prova de alucinações.

- Expansibilidade: O arquivo conhecimento_financeiro.json pode ser infinitamente expandido com novos termos e exemplos sem alterar uma linha de código.

- UX importa: Mesmo sem IA, o tom acolhedor, os emojis e a estrutura clara das respostas fazem o usuário se sentir bem atendido.

- Validação contínua: Testamos manualmente cada edge case para garantir que o agente nunca "quebra" ou responde algo inadequado.
