# notas e media de aluno
notas = []
for i in range(3):
    nota = float(input(f"digite a {i+1}ª nota: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("Média:", media)