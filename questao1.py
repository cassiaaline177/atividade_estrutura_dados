# Atividade 1 - Estrutura de Dados
# Nome: aline
# lista



numeros = []
for i in range (5):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)
print("Elemntos da lista: ", numeros)
print("Soma dos valores: ", sum(numeros))