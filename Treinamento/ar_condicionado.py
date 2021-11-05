'''
PROBLEMA A - Ar-Condicionado

INTEGRANTES:
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768
'''
entrada = input().upper()
if entrada == "FRIO":
    print(24)
elif entrada == "MUITO FRIO":
    print(20)
elif entrada == "EXTREMAMENTE FRIO":
    print(18)
elif entrada == "QUENTE":
    print(28)
else:
    print("COMANDO INVALIDO")