'''
PROBLEMA F - Jokenpô

INTEGRANTES:
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768
'''
jog1 = input()
jog2 = input()
if jog1 == jog2:
    print("Empate")
else:
    if jog1 == 'pedra' and jog2 == 'tesoura':
        print("Jogador 1")
    elif jog1 == 'tesoura' and jog2 == 'papel':
        print("Jogador 1")
    elif jog1 == 'papel' and jog2 == 'pedra':
        print("Jogador 1")
    else:
        print("Jogador 2")