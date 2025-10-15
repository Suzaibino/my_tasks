treino_do_dia = [
    {"tipo": "corrida", "duracao": "30", "intensidade": "alta"},
    {"tipo": "caminhada", "duracao": 40, "intensidade": "media"},
    {"tipo": "yoga", "duracao": "20", "intensidade": "baixa"},  # INVÁLIDO
    {"tipo": "natacao", "duracao": "abc", "intensidade": "alta"},  # INVÁLIDO
    {"tipo": "bicicleta", "duracao": "45", "intensidade": "media"}
]


def validar_exercicio(exercicio_bruto):
    tipos_validos = ["corrida", "caminhada", "natacao", "bicicleta"]
    instensidade_validas = ["baixa", "media", "alta"]
    erros = []
    detalhes = []
    for exercicio in exercicio_bruto:
        try:
            exercicio["duracao"] = int(exercicio["duracao"])
        except ValueError as e:
            erros.append(f"Erro ao converter duração: {e}")
        else:
            detalhes.append(exercicio)
            
            
            if exercicio["tipo"] not in tipos_validos :
                erros.append(f"Tipo de exercicio '{exercicio["tipo"]}' nao é valido")
                detalhes.pop()

            if exercicio["intensidade"] not in instensidade_validas :
                erros.append(f"Tipo de intensidade '{exercicio["tipo"]}' nao é valido")
                detalhes.pop()

    return detalhes, erros

def calcular_calorias(exercicio):
    calorias_por_minuto = [
    {"tipo": "corrida", "baixa": 8, "media": 10, "alta":13},
    {"tipo": "caminhada", "baixa": 3, "media": 5, "alta":7},
    {"tipo": "bicicleta", "baixa": 5, "media": 8, "alta":11},
    {"tipo": "natacao", "baixa": 7, "media": 9, "alta":12},
    ]

    exercicio_validos = validar_exercicio(exercicio)[0]
    for dicionario in exercicio_validos:
      for caloria_minuto in calorias_por_minuto:
            
            if dicionario["tipo"] == caloria_minuto["tipo"] and dicionario["intensidade"] == "baixa":
                calorias = caloria_minuto["baixa"] * dicionario["duracao"]
                dicionario["calorias"] = calorias

            elif dicionario["tipo"] == caloria_minuto["tipo"] and dicionario["intensidade"] == "media":
                calorias = caloria_minuto["media"] * dicionario["duracao"]
                dicionario["calorias"] = calorias
                
            elif dicionario["tipo"] == caloria_minuto["tipo"] and dicionario["intensidade"] == "alta":
                calorias = caloria_minuto["alta"] * dicionario["duracao"]
                dicionario["calorias"] = calorias
    return exercicio_validos
    
def processar_treino(lista_exercicios):
    calorias_totais = 0
    tempo_total = 0
    total_exercicios_validos = 0
    total_exercicios_invalidos = 0
    exercicios_validos = calcular_calorias(lista_exercicios)
    validacao = validar_exercicio(lista_exercicios)
    
    for calorias in exercicios_validos:
        calorias_totais += calorias["calorias"]
        tempo_total += calorias["duracao"]
    
    total_exercicios_invalidos = len(validacao[1])
    total_exercicios_validos = len(validacao[0])
    detalhes = validacao[0]
    erros = validacao[1]

    return detalhes, erros, total_exercicios_invalidos, total_exercicios_validos, tempo_total, calorias_totais


resultado = processar_treino(treino_do_dia)
print(f"Detalhes: {resultado[0]} \n Erros: {resultado[1]} \n Total de exercicios invalidos: {resultado[2]} \n Total de exercicios validos: {resultado[3]} \n Tempo total: {resultado[4]} \n Calorias totais: {resultado[5]}")