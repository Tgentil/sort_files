## Script de organização de arquivos

Este script em Python tem como objetivo organizar arquivos em um determinado diretório de acordo com um tamanho de lote pré-definido.

# Como usar

1. Abra o arquivo organizador_nfce.py em uma ide.
2. Na Pasta data coloque seus arquivos a serem coletados
2.1. Na variável DIRETORIO, defina o diretório onde os arquivos serão coletados.
3. Na variável LOTE_SIZE, defina o tamanho do lote (quantos arquivos serão movidos por lote).
4. Salve o arquivo e execute-o em seu terminal usando o comando python organizador_nfce.py.
5. O script irá contar quantos arquivos existem no diretório, e escrever o total de arquivos em um arquivo de texto chamado total_arquivos.txt.
6. O script irá criar pastas para cada lote de arquivos movidos de acordo com o tamanho definido em LOTE_SIZE, e moverá os arquivos para o diretório correspondente.

# Dica

Coloque seus arquivos em :
```python
# define o diretório onde os arquivos serão coletados
DIRETORIO = "./data"
if not os.path.exists(DIRETORIO):
    os.mkdir(DIRETORIO)
```

Ou então

Utilize :
```python
# define o diretório onde os arquivos serão coletados
DIRETORIO = r"path\para_o_seu\folder"
if not os.path.exists(DIRETORIO):
    os.mkdir(DIRETORIO)
```

Utilize `ctrl + shift + C` no Windowns ou `Command + Option + C` ( ⌥+ ⌘ + C ) no MacOs para copiar o path da pasta que você quer organizar e adicione entre aas aspas

# Observações
 
1. Os arquivos vão ser levados para a pasta que o código está sendo executado, você pode alterar o path da onde os arquivos seram movidos em :

```python
# define o diretório onde os lotes serão movidos
lote_dir = f"./lotes/lote_{LOTE_COUNT}"
```

2. A contagem de arquivos é feita antes do código mover os arquivos, caso você não se sinta seguro com o código, faça um backup dos arquivos antes de utilizalos e faça o relatório ser executado depois de mover os arquivos e não antes.

3. Não fiz tratamento de erro, o código pode gerar algum erro caso você tenha arquivos corrompidos, iguais, ou com mesmo nome, entre outros casos.

# Update 

Agora o script está lendo arquivos dentro de subpastas também

# Autor

* Thiago da Silveira Gentil

