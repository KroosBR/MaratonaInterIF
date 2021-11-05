lixo, valor = input().split("R$")
valor_pacote = float(valor)
moedas = [0.25, 0.10, 0.05, 0.01]
v_moedas = []
qtd_moedas = [int(qtd) for qtd in input().split()]

for i in range(len(moedas)):
    v_moedas.append(qtd_moedas[i] * moedas[i])


qtd_pacotes = int(sum(v_moedas) / valor_pacote)
valor_pacote *= qtd_pacotes

for i in range(len(v_moedas)):
    if valor_pacote % v_moedas[i] != 0:
        valor_pacote = valor_pacote % v_moedas[i]
        print(valor_pacote)
        qtd_moedas[i] = 0
print(qtd_moedas)
print(qtd_pacotes)
print(sum(qtd_moedas))