voos ={}
log = []
possiveis_status = ['Cancelado', 'Agendado']

def adicionar_voo(voos, codigo, destino, horario):
    voos[codigo] = {}
    voos[codigo]['destino'] = destino
    voos[codigo]['horario'] = horario
    voos[codigo]['status'] = 'Agendado'
    log.append(f'Voo {codigo} adicionado com sucesso.')

def alterar_status(voos, codigo, novo_status): 
    try:
        if novo_status in possiveis_status:
            voos[codigo]['status'] = novo_status
            log.append(f'Voo {codigo} teve seu status alterado para {novo_status}')
    except ValueError as a:
            log.append(f'Erro ao alterar o status: {a}')

def listar_voos(voos, status=None):
    if not status:
      print(voos)
    for codigo_voo, informacoes_voo in voos.items():
        try:
          if status in possiveis_status:
            if informacoes_voo['status'] == status:
                print(codigo_voo, informacoes_voo)
        except ValueError as a:
            log.append(f'Erro ao listar voos: {a}')

    log.append(f'Efetuou uma listagem dos voos')

def cancelar_voo(voos, codigo, alteracao = 'Cancelado'):
    voos[codigo]['status'] = alteracao
    log.append(f'Voo {codigo} foi cancelado.')

def consultar_voo(codigo):
    log.append(f'Fez uma consulta do voo {codigo}')
    print(voos[codigo])

adicionar_voo(voos, 'VB999', 'Canela', '06:00')
consultar_voo('VB999')
cancelar_voo(voos,'VB999')
print(listar_voos(voos))

with open('log.txt', 'w', encoding='utf-8') as f:
    for ocorrencia in log:
        f.write(f"{ocorrencia}\n")