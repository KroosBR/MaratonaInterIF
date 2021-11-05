'''
PROBLEMA B - Competição de vans!

INTEGRANTES:
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768
'''

tamanho, velocidade, tempo = map(int, input().split())
resultado = (velocidade*tempo)/(tamanho/1000)
print(int(resultado))