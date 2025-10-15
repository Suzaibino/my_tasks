def check(available_chars, testing_chars):
    contagem_available = {}
    for letra in available_chars:
        if letra in contagem_available:
            contagem_available[letra] += 1
        else:
            contagem_available[letra] = 1

    contagem_testing = {}
    for letra in testing_chars:
        if letra in contagem_testing:
            contagem_testing[letra] += 1
        else:
            contagem_testing[letra] = 1

    for letra in contagem_testing:
        if letra not in contagem_available or contagem_available[letra] < contagem_testing[letra]:
            return False
    return True


print(check("aaa", "a"))
