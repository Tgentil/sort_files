"""Script de organização de lotes de arquivos"""
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

# define o diretório onde os arquivos serão coletados
DIRETORIO = r"path\para_o_seu\folder"
if not os.path.exists(DIRETORIO):
    os.mkdir(DIRETORIO)

# lista todos os arquivos no diretório
arquivos = os.listdir(DIRETORIO)

# conta quantos arquivos existem no diretório
total_arquivos = sum(len(arquivos) for _, _, arquivos in os.walk(DIRETORIO))

# escreve o total de arquivos em um arquivo txt
with open("total_arquivos.txt", "w", encoding="utf-8") as arquivo_txt:
    arquivo_txt.write(f"Total de arquivos: {total_arquivos}")


# define o tamanho do lote (quantos arquivos serão movidos por vez)
LOTE_SIZE = 1000

# define o contador/nome dos lotes
LOTE_COUNT = 1

# define o diretório onde os lotes serão movidos
lote_dir = f"./lotes/lote_{LOTE_COUNT}"

# cria a pasta onde o primeiro lote será movido (caso ainda não exista)
if not os.path.exists(lote_dir):
    os.makedirs(lote_dir)

# move cada arquivo para o diretório do lote correspondente
for i, arquivo in enumerate(arquivos):
    if i % LOTE_SIZE == 0 and i != 0:
        # se atingir o tamanho do lote, cria uma nova pasta para o próximo lote
        LOTE_COUNT += 1
        lote_dir = f"./lotes/lote_{LOTE_COUNT}"
        os.makedirs(lote_dir)

    # move o arquivo para o diretório do lote correspondente
    shutil.move(os.path.join(DIRETORIO, arquivo), os.path.join(lote_dir, arquivo))


# Exibe uma mensagem de conclusão quando a tarefa é finalizada
print("Tarefa concluída!")
