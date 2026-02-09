# função recursiva

def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)

numero = int(input("Digite um número inteiro positivo: "))
print("Resultado:", soma_recursiva(numero))
