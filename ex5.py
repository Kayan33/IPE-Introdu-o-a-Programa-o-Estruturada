print("="*50)
print("NOTA FISCAL COMPRA". center(50))
print("="*50)

total_geral = 0
subtotal_geral = 0
desconto_geral = 0

for i in range (1,6):
    print("\n"+"-"*50)
    print(f"PRODUTO {i}".center(50))
    print("-"*50)
    
    # declarando varáveis e entradas
    desc_prod = input(f'Descrição do produto: ')
    qtd_adq = int(input(f'Quantidade adquirida: '))
    preco_prod = float(input(f'Preço Unitário: R$ '))

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
    desconto_msg = f"{int(desconto*100)}%"
    # printando resultados 

    print("\n"+"-"*50)
    print(f'Subtotal: R${subtotal:,.2f}')
    print(f'Desconto Aplicado ({desconto_msg}): R$-{desconto_valor:,.2f}')
    print(f'Total com Desconto: R${total:,.2f}')
    print("-"*50)

    # somando valores de 5 produtos e printando totais

    subtotal_geral += subtotal
    desconto_geral += desconto_valor
    total_geral += total
    
#resumo final da compra

print("\n"+"="*50)
print("RESUMO DA COMPRA".center(50))
print("="*50)
print(f'Subtotal Geral: R${subtotal_geral:,.2f}')
print(f'Desconto Total: R$-{desconto_geral:,.2f}')
print(f'Total A Pagar: R${total_geral:,.2f}')
print("\n"+"="*50)
