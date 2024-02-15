# Importa as bibliotecas necessárias
import os
import shutil
from tkinter.filedialog import askdirectory


# Função para solicitar a pasta de origem
def ask_pasta_origem():
    return askdirectory(title='Pasta Origem')


# Função para solicitar a pasta de destino
def ask_pasta_destino():
    return askdirectory(title='Pasta Destino')


# Dicionário com as regras para identificar o destino dos arquivos
regras_arquivos = {
    'ocrd': 'PN',
    'oitw': 'ITEM',
}


# Obtém a lista de arquivos na pasta de origem
def listar_arquivos(pasta_origem):
    return os.listdir(pasta_origem)


# Função para mover um arquivo para uma nova pasta
def mover_arquivo(nome_arquivo, pasta_origem, pasta_destino, nova_pasta):
    nome_completo_original = os.path.join(pasta_origem, nome_arquivo)
    nome_completo_final = os.path.join(pasta_destino, nova_pasta, nome_arquivo)
    caminho_nova_pasta = os.path.join(pasta_destino, nova_pasta)

    # Cria a nova pasta se não existir
    if not os.path.exists(caminho_nova_pasta):
        os.mkdir(caminho_nova_pasta)

    # Move o arquivo para a nova pasta
    shutil.move(nome_completo_original, nome_completo_final)


# Função principal que organiza os arquivos
def organizar_arquivos():
    pasta_origem = ask_pasta_origem()
    pasta_destino = ask_pasta_destino()
    lista_arquivos = listar_arquivos(pasta_origem)

    for nome_arquivo in lista_arquivos:
        for chave in regras_arquivos.keys():
            if chave in nome_arquivo:
                nova_pasta = regras_arquivos[chave]
                mover_arquivo(nome_arquivo, pasta_origem, pasta_destino, nova_pasta)


# Executa a função principal

organizar_arquivos()
