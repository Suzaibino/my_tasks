# Você tem uma lista de listas, onde cada sublista representa os resultados de um participante em uma série de testes. Cada sublista contém o ID do Participante (um número inteiro) e uma sequência de pontuações (números inteiros).
# Sua tarefa é realizar as seguintes operações:
# 1. Calcular Média e Filtrar: Para cada participante, calcule a média de suas pontuações. Em seguida, crie uma nova lista de listas contendo apenas os participantes cuja média de pontuação seja igual ou superior a 80. Cada sublista nesta nova lista deve conter [ID do Participante, Média de Pontuação].
# 2. Bônus por Consistência: Para os participantes que foram incluídos na lista do passo 1, verifique se a diferença entre a maior e a menor pontuação individual (dentro das pontuações originais de cada participante) é menor que 10. Se for, adicione um bônus de 5 pontos à sua Média de Pontuação. Atualize a lista com essas novas médias.
# 3. Ordenar: Ordene a lista resultante do passo 2 em ordem decrescente com base na Média de Pontuação (já com o bônus, se aplicável).
# 4. Identificar o Melhor: Qual é o ID do Participante do participante com a maior Média de Pontuação final?
# Apresente a lista final ordenada e o ID do participante com a maior média

resultados_testes = [
    [101, 85, 92, 78, 90],
    [102, 70, 65, 80, 75],
    [103, 95, 88, 91, 93],
    [104, 60, 72, 68, 55],
    [105, 80, 85, 82, 88],
    [106, 75, 70, 65, 72]
]

NOTA_DE_CORTE = 80.0


def mediator(lista):
    resultados_individuais = []
    for subtestes in lista:
        NOTAS_TESTES = subtestes[1:]
        media = sum(NOTAS_TESTES) / len(NOTAS_TESTES)
        if max(NOTAS_TESTES) - min(NOTAS_TESTES) < 10:
            media += 5
        if media >= NOTA_DE_CORTE:
            resultados_individuais.append([subtestes[0], media])
            resultados_individuais.sort(
                key=lambda resultados_individuais: resultados_individuais[1], reverse=True)
    print(resultados_individuais)
    print("O melhor participante: ", resultados_individuais[0])


mediator(resultados_testes)
