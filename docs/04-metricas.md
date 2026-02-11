# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1.Testes de funcionalidade: Verificar se cada comando/pergunta reconhecida retorna a resposta correta.

2.Testes com usuários reais: 3 a 5 pessoas testam e dão notas.

3.Cobertura da base de conhecimento: Quantas perguntas comuns o agente consegue responder?

---

## Métricas de Qualidade

Métrica	O que avalia	Como testar
Assertividade	O agente entendeu a pergunta e respondeu corretamente?	Fazer 10 perguntas que estão no JSON e verificar se acertou todas.
Cobertura	% de perguntas frequentes que o agente consegue responder	Listar 20 dúvidas comuns de iniciantes e ver quantas estão cadastradas.
Tom de voz	A resposta parece amigável e acessível?	Testadores avaliam de 1 a 5 se a linguagem é clara e acolhedora.
Segurança	O agente evitou dar recomendações ou "achar" respostas?	Fazer perguntas fora do escopo e ver se ele admite não saber.
Robustez	O sistema quebra com alguma pergunta estranha?	Testar entradas vazias, símbolos, perguntas muito longas.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

- Teste 1: Pergunta sobre produto
Pergunta: "O que é LCI?"

Resposta esperada: Explicação sobre LCI + exemplo.

Resultado: [✅] Correto [ ] Incorreto

- Teste 2: Simulação de rendimento
Pergunta: "Quanto rende 2000 em 10 meses a 0,8%?"

Resposta esperada: Cálculo correto de juros compostos.

Resultado: [✅] Correto [ ] Incorreto

- Teste 3: Pergunta fora da base
Pergunta: "O que é NFT?"

Resposta esperada: Fallback amigável ("Não sei, mas posso ajudar com...").

Resultado: [✅] Correto [ ] Incorreto

- Teste 4: Pergunta fora do escopo
Pergunta: "Me indica um bom banco?"

Resposta esperada: Explicação de que não faz recomendações.

Resultado: [✅] Correto [ ] Incorreto

- Teste 5: Entrada vazia
Pergunta: [usuário envia mensagem em branco]

Resposta esperada: Pedir para digitar algo ou manter silêncio (ideal: não quebrar).

Resultado: [✅] Correto [ ] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

✅ Respostas curtas com exemplos práticos.

✅ Tom informal e uso de emojis (💰📈😊).

✅ Cálculos instantâneos e corretos.

✅ Fallback educado ("Puts, essa não é minha área...").

**O que pode melhorar:**

🔧 Adicionar mais termos (ex: "dividendos", "IPCA", "reserva de emergência").

🔧 Melhorar detecção de variações (ex: "quanto renderia", "simula 1000 reais").

🔧 Incluir sugestão de leitura/canais no fallback.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

As pessoas entenderam a resposta?

Elas se sentiram acolhidas?

Elas aprenderam algo novo?

✅ Métrica mais importante: "Valeu, agora entendi!" — se isso aparecer no chat, o agente cumpriu seu papel.


Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
