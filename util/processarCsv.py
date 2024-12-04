import os

from frames import atividades, preferencia, placaMae


def get_sockets():
    try:
        gerar_csv_personalizado(preferencia.get_preferencia(), "Não possui")
    except:
        gerar_csv_personalizado("Indiferente", "Não possui")

    with open("arquivo_personalizado.csv", "r") as arquivo:
        sockets = [ socket.split(",")[4] for socket in arquivo ]
    return sorted(list(set(sockets)))

def gerar_csv_personalizado(preferencia, socket):
    comando = ""
    arquivo_csv = "cpus_filtro5.csv"
    arquivo_gerado = "arquivo_personalizado.csv"

    if preferencia == "Indiferente":
        if socket == "Não possui":
            comando = f"cp {arquivo_csv} {arquivo_gerado}"
        else:
            comando = f'grep "{socket}" {arquivo_csv} > {arquivo_gerado}'
    else:
        if socket == "Não possui":
            comando = f'grep "{preferencia}" {arquivo_csv} > {arquivo_gerado}'
        else:
            comando = f'grep -P "(?=.*\b{preferencia}\b)(?=.*\b{socket}\b)" {arquivo_csv} > {arquivo_gerado}'
    os.system(comando)

def gerar_lista_processadores():
    try:
        gerar_csv_personalizado(preferencia.get_preferencia(), placaMae.get_socket())
    except:
        gerar_csv_personalizado("Indiferente", "Não possui")

    with open("arquivo_personalizado.csv", "r") as arquivo:
        if atividades.get_classificacao_uso() == "Intenso":
            lista = [ x.split(",")[0] for x in arquivo if int(x.split(",")[6]) >= 6 ]
        elif atividades.get_classificacao_uso() == "Moderado":
            lista = [ x.split(",")[0] for x in arquivo if 4 <= int(x.split(",")[6]) <= 8 ]
        else:
            lista = [ x.split(",")[0] for x in arquivo if 1 <= int(x.split(",")[6]) <= 4]
    arquivo.close()
    return lista