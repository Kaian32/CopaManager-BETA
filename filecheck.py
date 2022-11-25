import os

#caminhos dos arquivos
path_equipes = "equipes.equipes"
path_jogos = "jogos.jogos"

#processo de checagen dos arquivos para verificar sua existência

isFile = os.path.isfile(path_equipes)

if isFile is False:
    print("Arquivo de equipes não encontrado! Criando um novo arquivo!")
    open ("equipes.equipes", "x")

isFile = os.path.isfile(path_jogos)

if isFile is False:
    print("Arquivo de jogos não encontrado! Criando um novo arquivo!")
    open ("jogos.jogos", "x")