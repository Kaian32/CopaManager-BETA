#Produzido por Kaian Vinicius, @Kaian32

#LIGA ISSO DEPOIS
import boot
from os import system #fazer certo em linux depois
import os #importando o OS como um todo logo
import time #importando o tempo
system('cls') #limpando comandos anteriores
print("Olá, seja bem vindo ao Copa Manager!") #mensagem de boas vindas

#open ("equipes.equipes", "a+") #SUBSTITUIDO POR FILECHECK#puxando o arquivo de equipes, caso não exista, ele será criado.
#open ("jogos.jogos", "a+") #SUBSTITUIDO POR FILECHECK#puxando o arquivo de jogos, caso não exista, ele será criado.

def leitor_equipes(): #faz a leitura do arquivo de equipes e monta uma lista a partir da mesma
    with open ("equipes.equipes", "r+") as valor:
        lista = []
        for equipes in valor:
            lista.append(equipes)
        return len(lista)

def leitor_jogos(): #faz a leitura do arquivo de jogos e monta uma lista a partir da mesma
    with open ("jogos.jogos", "r+") as valor:
        lista = []
        for equipes in valor:
            lista.append(equipes)
        return len(lista)

def nova_equipe(): #a def contém o processo de criação e salvamento de uma nova equipe
    system("cls")
    confirma = input("Deseja Realmente adicionar uma nova equipe?\n1) Sim\n2) Não\n")
    if (confirma == "1"):
        with open ("equipes.equipes", "a+") as equipes:
            equipes.write(str(input("Insira o nome da equipe: ").upper()))
            equipes.write("\n")
    system("cls")

def novo_jogo():
    system("cls")
    confirma = input("Deseja Realmente adicionar um novo jogo?\n1) Sim\n2) Não\n")
    if (confirma == "1"):
        with open ("jogos.jogos", "a+") as equipes:
            equipes.write(str(input("Insira o resultado do jogo: ").upper()))
            equipes.write("\n")
    system("cls")

while True:
    print("Selecione uma das opções abaixo:")
    print("1) SAIR\nFecha o aplicativo.")
    print("2) Nova Equipe\nAdiciona uma nova equipe ao dados.")
    print("3) Novo Jogo\nAdiciona um novo jogo aos dados.")
    print(f'\n\nTotal de Jogos = {leitor_jogos()}')
    print(f'Total de Equipes = {leitor_equipes()}')


    escolha = input("Selecione uma opção: ")
    escolha = escolha.strip()

    match escolha:
        case "1":
            system("cls")
            break
        case "2":
            nova_equipe()
        case "3":
            novo_jogo()
        case other:
            system("cls")
            print("Esta opção não é válida! Tente novamente!")
            time.sleep(1)
            system("cls")