NumeroInt = int(input("Digite um número inteiro: "))

print("\n50 números anteriores:")
for i in range(NumeroInt - 50, NumeroInt +1):
    print(i, end=" ")

print("\n\n50 números posteriores:")
for i in range(NumeroInt, NumeroInt + 51):
    print(i, end=" ")
