import json

dados = [
    '{"sensor": "A1", "temperatura": "22.5", "umidade": "55"}',
    {"sensor": "B2", "temperatura": 28, "umidade": 70},
    '{"sensor": "C3", "temperatura": "abc", "umidade": "65"}',  # temperatura inválida
    {"sensor": "D4", "temperatura": 38, "umidade": 85},  # CRÍTICO!
    '{"sensor": "E5", "temperatura": "25", "umidade": "150"}',  # umidade inválida
    {"sensor": "F6", "temperatura": 23.5, "umidade": 60},
    # temperatura fora do range
    '{"sensor": "G7", "temperatura": "-20", "umidade": "50"}',
    {"sensor": "H8", "temperatura": 26, "umidade": 58},
    "dados corrompidos",  # não é JSON válido
    {"sensor": "I9", "temperatura": 36.5, "umidade": 75},  # CRÍTICO!
]


def processar_leituras(dados_sensores):
    leituras_processadas = {}
    dados_processados = []
    alertas_criticos = []
    leituras_validas = []
    temperatura_media = 0
    umidade_media = 0
    erros = []

    for leitura in dados_sensores:
        conversao = leitura
        if isinstance(leitura, str):
            try:
                conversao = json.loads(leitura)
            except json.JSONDecodeError as e:
                erros.append(f"Erro ao processar JSON: {e}")
                continue
        dados_processados.append(conversao)

    for manipulacao in dados_processados:
        try:
            manipulacao['temperatura'] = float(manipulacao.get('temperatura'))
            manipulacao['umidade'] = float(manipulacao.get('umidade'))
        except ValueError as e:
            erros.append(f"{manipulacao['sensor']}: Erro ao converter: {e}")
            continue

        leituras_validas.append(manipulacao)

        if manipulacao["temperatura"] < -10 or manipulacao["temperatura"] > 50:
            erros.append(
                f"{manipulacao["sensor"]}: temperatura {manipulacao["temperatura"]} fora do range de -10 a 50 ")

            leituras_validas.pop()

        elif manipulacao["umidade"] < 0 or manipulacao["umidade"] > 100:
            erros.append(
                f"{manipulacao["sensor"]}: umidade {manipulacao["umidade"]} fora do range de 0 a 100 ")
            leituras_validas.pop()

        elif manipulacao['temperatura'] > 35 and manipulacao['umidade'] > 80:
            alertas_criticos.append(
                f"{manipulacao["sensor"]}: temperatura {manipulacao["temperatura"]}°C e umidade {manipulacao['umidade']}")
        elif manipulacao['temperatura'] > 35:
            alertas_criticos.append(
                f"{manipulacao["sensor"]}: temperatura {manipulacao["temperatura"]}°C acima do limite")

    valores_temp = [temp['temperatura'] for temp in leituras_validas]
    temperatura_media = sum(valores_temp) / len(valores_temp)

    valores_umid = [umid['umidade'] for umid in leituras_validas]
    umidade_media = sum(valores_umid) / len(valores_umid)

    leituras_processadas['leituras_validas'] = leituras_validas
    leituras_processadas['alertas_criticos'] = alertas_criticos
    leituras_processadas['temperatura_media'] = (f'{temperatura_media:.2f}')
    leituras_processadas['umidade_media'] = (f'{umidade_media:.2f}')
    leituras_processadas['erros'] = erros

    return leituras_processadas


print(processar_leituras(dados))
