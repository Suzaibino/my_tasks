precos_brutos = [25, "10.50", 5.99, "30", "grátis", 12, "20.00", "N/A", 1.99]

def processar_e_ordenar_precos(lista_de_precos):
    precos_ordenados = []
    for precos in lista_de_precos:
        try:
            precos = float(precos)
        except ValueError:
            continue
        precos_ordenados.append(precos)
    precos_ordenados.sort()
    print(precos_ordenados)

processar_e_ordenar_precos(precos_brutos)
