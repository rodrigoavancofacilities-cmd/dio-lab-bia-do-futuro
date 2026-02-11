import streamlit as st
import json
import re
from funcoes_calculo import calcular_juros_compostos

# ---------- CARREGAR BASE DE CONHECIMENTO ----------
@st.cache_data
def carregar_conhecimento():
    with open("conhecimento_financeiro.json", "r", encoding="utf-8") as f:
        return json.load(f)

conhecimento = carregar_conhecimento()

# ---------- CONFIGURAÇÃO DA PÁGINA ----------
st.set_page_config(page_title="Orientar - Educação Financeira", page_icon="💰")
st.title("💰 Orientar")
st.markdown("E aí! Sou o **Orientar**. Manda sua dúvida financeira que eu tento ajudar :)")

# ---------- INICIALIZAR HISTÓRICO ----------
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Exibir histórico
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- FUNÇÃO PARA DETECTAR CÁLCULO ----------
def extrair_calculo(texto):
    """
    Detecta padrões como "quanto rende 1000 em 6 meses a 1%" e retorna parâmetros.
    Retorna (valor, meses, taxa) ou None se não encontrar.
    """
    texto = texto.lower()
    # Padrão: "rende X em Y meses a Z%"
    padrao = r"(?:rende|renderia|render|r\$?)\s*(\d+[.,]?\d*)\s*(?:reais?)?\s*(?:em|por|durante)?\s*(\d+)\s*(?:meses?|mêses?|m|ano|anos)?\s*(?:a|de)?\s*(\d+[.,]?\d*)\s*%"
    match = re.search(padrao, texto)
    if match:
        valor = float(match.group(1).replace(",", "."))
        meses = int(match.group(2))
        taxa = float(match.group(3).replace(",", "."))
        return valor, meses, taxa
    return None

# ---------- FUNÇÃO PARA ENCONTRAR PALAVRA-CHAVE ----------
def encontrar_termo(texto):
    texto_lower = texto.lower()
    for termo in conhecimento.keys():
        if termo in texto_lower:
            return termo
    return None

# ---------- PROCESSAR PERGUNTA ----------
def responder(pergunta):
    # 1. Verifica se é cálculo
    calc = extrair_calculo(pergunta)
    if calc:
        valor, meses, taxa = calc
        montante, rendimento = calcular_juros_compostos(valor, taxa, meses)
        return f"📈 **Resultado:** R$ {valor:,.2f} em {meses} meses a {taxa}% ao mês.\n\n**Montante final:** R$ {montante:,.2f}\n**Rendimento:** R$ {rendimento:,.2f}\n\n*Cálculo com juros compostos.*"
    
    # 2. Verifica se é dúvida sobre produto/conceito
    termo = encontrar_termo(pergunta)
    if termo:
        dados = conhecimento[termo]
        resposta = dados["resposta"]
        if "exemplo" in dados:
            resposta += f"\n\n📌 **Exemplo:** {dados['exemplo']}"
        return resposta
    
    # 3. Não sei responder
    return "Puts, essa não é minha área. Mas posso te explicar sobre poupança, CDB, Tesouro, juros compostos ou fazer simulações de rendimento! 😊"

# ---------- ENTRADA DO USUÁRIO ----------
pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    # Adiciona pergunta ao histórico
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    # Gera resposta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            resposta = responder(pergunta)
            st.markdown(resposta)
    
    # Adiciona resposta ao histórico
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
