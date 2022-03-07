from random import randint
from time import sleep

computador = randint(0,2)

opcoes = ["Pedra","Papel","Tesoura"]

jogador = int(input("""Escolha sua Jogada:
[0]Pedra
[1]Papel
[2]Tesoura \n"""))
print("jo")
sleep(1)

print("ken")
sleep(1)

print("PÔ")


if jogador==0:
    if computador==0:
        print("Empate, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))

if jogador==1:
    if computador==1:
        print("Empate, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))


if jogador==2:
    if computador==2:
        print("Empate, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))


if jogador==0:
    if computador==1:
        print("Computador Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))


if jogador==0:
    if computador==2:
        print("Jogador Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))


if jogador==1:
    if computador==0:
        print("Jogador Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))

if jogador==1:
    if computador==2:
        print("Computador Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))

if jogador==2:
    if computador==0:
        print("Computador Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))


if jogador==2:
    if computador==1:
        print("Jogador Venceu Venceu, jogador foi em {}".format(opcoes[jogador])," e computador foi {}".format(opcoes[computador]))




