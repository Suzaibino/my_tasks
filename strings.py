def processar_mensagem(mensagem_bruta, usuario):
    """
    Processa mensagem de chat aplicando limpeza e análise.
    """

    # Lista de palavrões
    palavroes = ["idiota", "burro", "estupido"]

    # 1. LIMPAR USUÁRIO 
    usuario_limpo = usuario.strip().title()

    # 2. LIMPAR MENSAGEM
    mensagem_limpa = mensagem_bruta.strip()

    #remover múltiplos espaços
    mensagem_limpa = " ".join(mensagem_limpa.split())

    #remover caracteres repetidos
    caractere_anterior = ""
    filtro_mensagem = ""
    for caractere in mensagem_limpa:
        if caractere == caractere_anterior and caractere in "!?.,*@#$":
            continue
        else:
            filtro_mensagem += caractere
            caractere_anterior = caractere
    mensagem_limpa = filtro_mensagem

    # 3. CENSURAR PALAVRÕES
    mensagem_censurada = mensagem_limpa
    for palavrao in palavroes:
        mensagem_censurada = mensagem_censurada.replace(palavrao, "*******")

    # 4. DETECTAR TIPO
    tipo = "normal"
    if mensagem_limpa.endswith("?"):
        tipo = "pergunta"
    if mensagem_limpa.startswith("/"):
        tipo = "comando"

    # 5. VERIFICAR SE É GRITO
    eh_grito = False
    letras_maiusculas = sum(
        1 for letra in mensagem_limpa if mensagem_limpa.isupper())
    porcentagem = (letras_maiusculas / len(mensagem_limpa)) * 100
    if porcentagem > 30:
        eh_grito = True

    # 6. EXTRAIR INFORMAÇÕES
    palavras = len(mensagem_limpa.split(" "))
    caracteres = len(mensagem_limpa)

    #encontrar hashtags
    hashtags = []
    for palavra in mensagem_limpa.split():
        if palavra.startswith("#"):
            hashtags.append(palavra)

    #encontrar menções
    mencoes = []
    for palavra in mensagem_limpa.split():
        if palavra.startswith("@"):
            mencoes.append(palavra)
            palavras -= 1

    # 7. MONTAR RESULTADO
    resultado = {
        "usuario": usuario_limpo,
        "mensagem_original": mensagem_bruta,
        "mensagem_limpa": mensagem_limpa,
        "mensagem_censurada": mensagem_censurada,
        "tipo": tipo,
        "eh_grito": eh_grito,
        "estatisticas": {
            "palavras": palavras,
            "caracteres": caracteres,
            "hashtags": hashtags,
            "mencoes": mencoes
        }
    }

    return resultado


# TESTES
print("=== TESTE 1 ===")
msg1 = "  OLÁ @maria  como você está???  #feliz  "
user1 = "  joao  silva  "
print(processar_mensagem(msg1, user1))

print("\n=== TESTE 2 ===")
msg2 = "/ajuda comandos disponíveis"
user2 = "ana costa"
print(processar_mensagem(msg2, user2))

print("\n=== TESTE 3 ===")
msg3 = "Você é um idiota!!!! burro!!!"
user3 = "pedro santos"
print(processar_mensagem(msg3, user3))

print("\n=== TESTE 4 ===")
msg4 = "hoje está lindo #bomdia #segunda"
user4 = "maria oliveira"
print(processar_mensagem(msg4, user4))
