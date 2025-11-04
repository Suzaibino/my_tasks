from datetime import time, datetime, timedelta
import uuid

voos = {}
passagens_compradas = {}
log = []
POSSIVEIS_STATUS = ['Cancelado', 'Agendado', 'Alterado', 'Atrasado']
# CGH - SP, SDU - RJ, BSB - BRASILIA, CNF - BH, POA - PORTO
BLOCK_TIMES = {
    "CGHxSDU": "01:22:00",
    "CGHxBSB": "02:02:00",
    "CGHxCNF": "01:32:00",
    "POAxCGH": "02:02:00",
    "SDUxBSB": "02:02:00",
    "SDUxCNF": "01:22:00",
    "POAxSDU": "02:22:00",
    "BSBxCNF": "01:27:00",
    "POAxBSB": "02:37:00",
    "POAxCNF": "02:12:00",
}
CIDADES_POSSIVEIS = ['CGH', 'SDU', 'BSB', 'CNF', 'POA']
ORIGEM = 'POA'


def to_timedelta(hms: str) -> timedelta:
    h, m, s = map(int, hms.split(":"))
    return timedelta(hours=h, minutes=m, seconds=s)


def fmt(td: timedelta) -> str:
    total = int(td.total_seconds())
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def adicionar_voo(codigo, horario, limite_bagagem, ocupacao_total, valor_passagem, aeroporto_final, escalas=[], ):
    if codigo in voos:
        log.append('Esse voo já existe')
        return False
    ultima_escala = ORIGEM
    estimativa_de_tempo = timedelta()
    for escala in escalas:
        rota = [(ultima_escala + 'x' + escala),(escala + 'x' + ultima_escala)]
        for possiveis_rotas in rota:
            try:  
                estimativa_de_tempo += (to_timedelta(BLOCK_TIMES[possiveis_rotas]))
            except KeyError:
                continue
        ultima_escala = escala
    rota_final = [(ultima_escala + 'x' + aeroporto_final), (aeroporto_final + 'x' + ultima_escala)]
    for possiveis_rotas_finais in rota_final:
        try:
            estimativa_de_tempo += (to_timedelta(BLOCK_TIMES[possiveis_rotas_finais]))
        except KeyError:
            continue
    voos[codigo] = {
        'destino': aeroporto_final,
        'horario': horario,
        'status': 'Agendado',
        'tempo aproximado': fmt(estimativa_de_tempo),
        'limite de bagagem': limite_bagagem,
        'ocupação total': ocupacao_total,
        'quantidade atual de passageiros': 0,
        'valor da passagem': valor_passagem
    }
    log.append(f'Voo {codigo} adicionado com sucesso')


def alterar_status(codigo, novo_status):
    if codigo not in voos:
        log.append('Esse voo não existe')
        return False
    if novo_status in POSSIVEIS_STATUS:
        voos[codigo]['status'] = novo_status
        log.append(f'Voo {codigo} teve seu status alterado para {novo_status}')
    else:
        log.append(f'O status {novo_status} não está disponível.')


def listar_voos(status=None):
    if not status:
        print(voos)
    for codigo_voo, informacoes_voo in voos.items():
        if status in POSSIVEIS_STATUS:
            if informacoes_voo['status'] in status:
                print(codigo_voo, informacoes_voo)
            else:
                log.append(f'Erro ao listar voos')
    log.append(f'Efetuou uma listagem dos voos')


def cancelar_voo(codigo):
    alterar_status(codigo, 'Cancelado')


def consultar_voo(codigo):
    if codigo not in voos:
        log.append('Esse código não existe')
        return False
    else:
        print(voos[codigo])
        log.append(f'Consultou o voo {codigo}')

def comprar_passagem(codigo, nome_do_passageiro, numero_de_bagagens):
    if codigo not in voos:
        log.append('Esse código não existe para ser comprado')
    if 0 < numero_de_bagagens > 5:
        log.append(f'A quantidade de bagagem miníma é 0 e o máximo 5, atualmente {numero_de_bagagens}')
    voos[codigo]['limite de bagagem'] -= numero_de_bagagens
    id_compra = uuid.uuid4().hex
    passagens_compradas[id_compra] = {
        'Codigo do voo': codigo,
        'Nome': nome_do_passageiro,
        'Status do pagamento': 'Pendente',
        'Bagagens': numero_de_bagagens
    }
    log.append(f'O passageiro {nome_do_passageiro} comprou uma passagem para o voo {codigo}, levando {numero_de_bagagens}, código de compra {id_compra}')
    return id_compra


def pagar_passagem(id_compra):
    passagens_compradas[id_compra]['Status do pagamento'] = 'Pago'
    codigo_de_voo = passagens_compradas[id_compra]['Codigo do voo']
    voos[codigo_de_voo]['quantidade atual de passageiros'] += 1
    log.append(f'A passagem {passagens_compradas[id_compra]} foi paga.')

def testar_codigo():
    adicionar_voo('VB999', '06:00', 100, 300, 500.00, 'BSB')
    passagem = comprar_passagem('VB999', 'VINICIUS', 2)
    adicionar_voo('TNC000', '23:00', 100, 300, 500.00, 'BSB', ['SDU', 'CGH'])
    consultar_voo('VB999')
    alterar_status('VB999', 'Atrasado')
    cancelar_voo('TNC000')
    consultar_voo('VB99')
    pagar_passagem(passagem)
    print(listar_voos())
testar_codigo()

with open('log.txt', 'w', encoding='utf-8') as f:
    for ocorrencia in log:
        f.write(f"{ocorrencia}\n")
