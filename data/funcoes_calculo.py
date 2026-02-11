def calcular_juros_compostos(valor_inicial, taxa_mensal, meses):
    """
    Calcula o montante final com juros compostos.
    
    Parâmetros:
    - valor_inicial: float, valor aplicado
    - taxa_mensal: float, taxa percentual ao mês (ex: 1 para 1%)
    - meses: int, número de meses
    
    Retorna:
    - montante: float, valor final
    - rendimento: float, lucro obtido
    """
    taxa = taxa_mensal / 100
    montante = valor_inicial * (1 + taxa) ** meses
    rendimento = montante - valor_inicial
    return round(montante, 2), round(rendimento, 2)
