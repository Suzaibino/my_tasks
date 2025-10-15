dados = [
    {"tipo": "deposito", "valor": "500.50", "data": "01/01/2024"},
    {"tipo": "saque", "valor": 200, "data": "02/01/2024"},
    {"tipo": "deposito", "valor": "abc", "data": "03/01/2024"},  # inválido
    {"tipo": "saque", "valor": "-50", "data": "04/01/2024"},  # inválido
    {"tipo": "investimento", "valor": 100, "data": "05/01/2024"},  # tipo inválido
    {"tipo": "deposito", "valor": 300.75, "data": "06/01/2024"},
]


def processar_transacoes(dados_brutos):
    processamento_final_dados = {}
    saldo_final = 1000
    transacoes_validas = []
    transacoes_invalidas = []

    for dicionario in dados_brutos:
        valor = 0
        try:
            valor = float(dicionario["valor"])
        except ValueError as e:
            transacoes_invalidas.append(e)
        else:
            if valor > 0:
                if dicionario["tipo"] == "deposito":
                    saldo_final += valor
                    transacoes_validas.append(
                        {"tipo": dicionario["tipo"], "valor": valor, "data": dicionario["data"]})
                elif dicionario["tipo"] == "saque":
                    saldo_final -= valor
                    transacoes_validas.append(
                        {"tipo": dicionario["tipo"], "valor": valor, "data": dicionario["data"]})
                else:
                    transacoes_invalidas.append(
                        f"Erro: tipo de transação '{dicionario["tipo"]}' não suportado")
            else:
                transacoes_invalidas.append(
                    "Erro: valor de saque deve ser positivo")
    processamento_final_dados["saldo_final"] = saldo_final
    processamento_final_dados["transacoes_invalidas"] = transacoes_invalidas
    processamento_final_dados["transacoes_validas"] = transacoes_validas

    return processamento_final_dados


print(processar_transacoes(dados))
