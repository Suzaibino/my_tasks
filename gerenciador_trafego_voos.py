from datetime import time, datetime, timedelta

voos = {}
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

def to_timedelta(hms: str) -> timedelta:
    h, m, s = map(int, hms.split(":"))
    return timedelta(hours=h, minutes=m, seconds=s)

def fmt(td: timedelta) -> str:
    total = int(td.total_seconds())
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def adicionar_voo(codigo, destino, horario, origem, aeroporto_final, escala = None):
    if codigo in voos:
        log.append('Esse voo já existe')
        return False
    if not all(cidades in CIDADES_POSSIVEIS for cidades in (origem, aeroporto_final, escala) if cidades):
        log.append('Cidade indisponível')
        return False
    if not escala:
        identificar_voo_sem_escala = (origem + "x" + aeroporto_final)
        estimativa_de_tempo = to_timedelta(BLOCK_TIMES[identificar_voo_sem_escala])
        voos[codigo] = {
            'destino': destino,
            'horario': horario,
            'status': 'Agendado',
            'tempo aproximado': fmt(estimativa_de_tempo)
        }
        log.append(f'Voo {codigo} adicionado com sucesso')
    else:
        identificar_com_escala = (origem + "x" + escala)
        escala_destino_final = (escala + "x" + aeroporto_final)
        estimativa_de_tempo = (to_timedelta(BLOCK_TIMES[identificar_com_escala]) + to_timedelta(BLOCK_TIMES[escala_destino_final]))
        voos[codigo] = {
            'destino': destino,
            'horario': horario,
            'status': 'Agendado',
            'tempo aproximado': fmt(estimativa_de_tempo)
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


adicionar_voo('VB999', 'Canela', '06:00', 'POA', 'BSB', 'CGH')
adicionar_voo('AB123', 'Sao Paulo', '01:00', 'POA', 'BSB')
consultar_voo('VB999')
alterar_status('VB999', 'Atrasado')
print(listar_voos())
cancelar_voo('VB999')
consultar_voo('VB99')


with open('log.txt', 'w', encoding='utf-8') as f:
    for ocorrencia in log:
        f.write(f"{ocorrencia}\n")
