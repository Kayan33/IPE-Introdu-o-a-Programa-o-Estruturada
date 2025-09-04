
dia =  int(input("digite o dia do seu nascimento: "))
mes = int(input("digite o mês do seu nascimento: "))
ano = int(input("digite o ano do seu nascimento: "))


diaatual = 4
mesatual = 9
anoatual = 2025

idade = anoatual - ano
diasDeVida = idade * 365

print("Você tem " + str(idade) + " anos e " + str(diasDeVida) + " dias de vida")