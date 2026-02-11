# Base de Conhecimento

## Dados Utilizados

Dados Utilizados
Arquivo	Formato	Utilização no Agente

- conhecimento_financeiro.json	JSON	Armazena respostas prontas para perguntas frequentes sobre produtos e conceitos financeiros (ex: "o que é CDB?", "diferença entre débito e crédito")

- funcoes_calculo.py	Python	Contém as funções de cálculo (juros compostos, valor futuro) – não é um arquivo de dados, mas sim a lógica embutida no agente

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Criamos do zero um arquivo conhecimento_financeiro.json com as perguntas e respostas mais comuns para o público iniciante.
Cada entrada contém:

termo: palavra‑chave ou expressão associada

resposta: texto curto, com analogia simples

exemplo: (opcional) um exemplo numérico ou situação prática

Exemplo de expansão manual:
Incluímos explicações para CDB, poupança, Tesouro Selic, LCI, LCA, ações, fundos imobiliários, diferença entre débito/crédito, e juros compostos. Todas as respostas foram escritas em linguagem acessível e revisadas para evitar jargões.



---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O arquivo conhecimento_financeiro.json é carregado uma única vez, na inicialização da aplicação Streamlit, usando a biblioteca json padrão do Python. O conteúdo é armazenado em um dicionário em memória para acesso rápido durante toda a sessão.

import json

with open("conhecimento_financeiro.json", "r", encoding="utf-8") as f:
    base_conhecimento = json.load(f)

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Não utilizamos LLM/prompt complexo. A abordagem é totalmente baseada em regras:

O agente recebe a mensagem do usuário.

Uma função de pré‑processamento extrai palavras‑chave (ex: "cdb", "poupança", "juros").

O dicionário base_conhecimento é consultado:

Se a palavra‑chave existir → retorna a resposta pronta.

Se for uma solicitação de cálculo (ex: "quanto rende 1000 em 6 meses a 1%") → aciona a função juros_compostos(principal, taxa, meses) e retorna o valor calculado + explicação breve.

Se nenhuma correspondência for encontrada → resposta de fallback ("Não sei, mas posso ajudar com outras perguntas!").

Essa estratégia elimina completamente o risco de alucinação e mantém o código simples, adequado para iniciantes.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Como o agente não mantém estado entre perguntas e não utiliza dados de clientes, não há um "contexto" dinâmico formatado.
Em vez disso, mostramos a estrutura da base de conhecimento utilizada:

```
{
  "cdb": {
    "resposta": "Pensa no CDB como um empréstimo pro banco. Você empresta seu dinheiro e eles te devolvem com juros depois de um tempo. É mais seguro que ações, mas rende mais que poupança.",
    "exemplo": "R$ 1.000 em um CDB de 100% do CDI rende cerca de R$ 1.080 em 1 ano (depende da taxa)."
  },
  "poupanca": {
    "resposta": "Poupança é o jeito mais básico de guardar dinheiro. Rendimento baixo (0,5% ao mês + TR), mas você pode sacar quando quiser e é garantida pelo FGC até R$ 250 mil.",
    "exemplo": "R$ 1.000 na poupança rendem aproximadamente R$ 1.006 em 1 mês."
  },
  "juros_compostos": {
    "resposta": "Juros compostos são os famosos 'juros sobre juros'. No primeiro mês rende 1 real, no segundo rende em cima do que já tinha (principal + juros). É assim que o dinheiro cresce mais rápido com o tempo.",
    "exemplo": "R$ 1.000 a 1% ao mês: mês 1 = R$ 1.010, mês 2 = R$ 1.020,10, mês 3 = R$ 1.030,30..."
  }
}
```
