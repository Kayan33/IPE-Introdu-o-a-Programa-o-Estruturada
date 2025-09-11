ra = str(input("Digite seu RA: "))
nome = str(input("Digite seu nome: "))
curso = str(input("Digite seu curso: "))
disciplina = str(input("Digite sua disciplina: "))

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))

media = (nota1+nota2)/2

if (media >= 7):
    print(f'Aluno aprovado!\nMédia: {media:.2f}')
else:
    print(f'Aluno reprovado!\nmedia: {media:.2f}')
    