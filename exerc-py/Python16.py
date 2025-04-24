soma = 0
contador = 0

while contador < 30:
    try:
        numero = int(input(f"Digite o {contador + 1}º número par entre 1 e 50: "))

        if 1 <= numero <= 50 and numero % 2 == 0:
            soma += numero
            contador += 1
        else:
            print("Número inválido! O número deve ser par e entre 1 e 50.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

media = soma / 30
print(f"\nA média dos 30 números pares é: {media:.2f}")