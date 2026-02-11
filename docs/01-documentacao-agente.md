# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Pessoas jovens querem aprender sobre dinheiro, mas:

- Apps de banco só querem vender produto

- Textos na internet são longos e cheios de palavras difíceis

- Não têm com quem perguntar coisas "bobas"

### Solução
> Como o agente resolve esse problema de forma proativa?

Um chatbot simples que:

- Explica o que é CDB, poupança, juros, etc. em 3 frases

- Faz contas rápidas (ex: "quanto rende R$1000 em 1 ano?")

- Fala como gente normal, sem termos técnicos
  
### Público-Alvo
> Quem vai usar esse agente?

- Jovens de 16 a 25 anos

- Quem nunca investiu antes

- Quem tem vergonha de perguntar no banco

---

## Persona e Tom de Voz

### Nome do Agente
Orientar

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Paciente, repete sem reclamar

- Fala igual ser humano, não robô

- Usa analogias bestas mas que funcionam

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, leve, com emojis simples 😊💰

### Exemplos de Linguagem
- Começo	"E aí! Sou o Orientar. Manda sua dúvida financeira que eu tento ajudar :)
- Explicando	"Pensa no CDB como um empréstimo pro banco. Você empresta, eles devolvem com juros."
- Conta	"Deixa eu calcular aqui rapidinho..."
- Não sabe	"Puts, essa não é minha área. Mas posso te explicar outras coisas!"

---

## Arquitetura

### Diagrama

flowchart TD
    Início[Usuário] -->|Pergunta| Agente{Orientar}
    Agente --> Verifica1{É pergunta de conta?}
    Verifica1 -->|Sim| Calcula[Faz cálculo com função Python]
    Calcula --> Responde[Responde com resultado]
    
    Verifica1 -->|Não| Verifica2{É dúvida sobre produto?}
    Verifica2 -->|Sim| Busca[Busca resposta pronta no .json]
    Busca --> Responde
    
    Verifica2 -->|Não| NaoSei[Não sei responder]
    NaoSei --> Responde

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Python puro |
| Base de Conhecimento | .json com perguntas e respostas prontas |
| Validação | Funções simples de juros |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- ✅ Agente só responde com base nos dados fornecidos
Utiliza um arquivo .json com respostas prontas para conceitos financeiros. Para cálculos, executa funções Python dedicadas. Não gera respostas "criativas" fora desse escopo.

- ✅ Respostas incluem fonte da informação
Quando relevante, indica que a informação é de conhecimento público (ex: "Segundo o Banco Central...") ou que se trata de um exemplo ilustrativo.

- ✅ Quando não sabe, admite e redireciona
Frases como "Puts, essa não é minha área. Mas posso te explicar outras coisas!" deixam claro o limite do agente.

- ✅ Não faz recomendações de investimento
O Orientar nunca sugere "compre isso" ou "invista naquilo". Explica apenas o funcionamento dos produtos.

### Limitações Declaradas
> O que o agente NÃO faz?

O que o agente NÃO faz?

- ❌ Não recomenda produtos financeiros – nem CDB, nem ações, nem criptomoedas.

- ❌ Não acessa contas bancárias, extratos ou dados pessoais – o chat é 100% anônimo.

- ❌ Não oferece consultoria personalizada – as respostas são genéricas e educativas.

- ❌ Não analisa investimentos de alto risco – não fala sobre day trade, opções, derivativos.

- ❌ Não substitui um profissional certificado – para decisões importantes, recomenda-se buscar um assessor ou planejador financeiro.

- ❌ Não armazena informações do usuário – não há cadastro, login nem memória entre sessões.

- ❌ Não atende emergências – não ajuda com negociação de dívidas, problemas com bancos ou situações de estresse financeiro.

