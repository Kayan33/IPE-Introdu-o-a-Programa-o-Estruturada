print("-----NOTA FISCAL COMPRA----")

total_geral = 0
subtotal_geral = 0
desconto_geral = 0


for i in range (1,6):
    print(f'Produto {i}')
    # declarando varáveis e entradas
    desc_prod = input(f'Digite a descrição do produto: ')
    qtd_adq = int(input(f'Digite a quantidade adquirida: '))
    preco_prod = float(input(f'Digite o preço: R$ '))

    # calculando subtotal, descontos e total

    subtotal = (qtd_adq*preco_prod)

    if qtd_adq <= 5:
        desconto = 0.02
    elif qtd_adq > 5 and qtd_adq <= 10:
        desconto = 0.03
    else:
        desconto = 0.05

    desconto_valor = (subtotal*desconto)
    total = subtotal-(subtotal*desconto)

    # printando resultados 

    print("---------------------------")
    print(f'Subtotal Produto: {subtotal:.2f}R$')
    print(f'Desconto: -{desconto_valor:.2f}R$')
    print(f'Total Produto: {total:.2f}R$')
    print("---------------------------")

    # somando valores de 5 produtos e printando totais

    subtotal_geral += subtotal
    desconto_geral += desconto_valor
    total_geral += total

print("---------------------------")
print("-----RESUMO DA COMPRA------")
print(f'Subtotal Geral: {subtotal_geral:.2f}R$')
print(f'Desconto Geral: -{desconto_geral:.2f}R$')
print(f'Total Geral: {total_geral:.2f}R$')
print("---------------------------")


