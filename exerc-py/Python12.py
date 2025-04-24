n = int(input("Digite um número: "))

contador = 0

for i in range(1, n):
    print(f"\nOperações com o número {i}:")
    
    soma = n + i
    print(f"{n} + {i} = {soma}")
    contador += 1

    subtracao = n - i
    print(f"{n} - {i} = {subtracao}")
    contador += 1

    multiplicacao = n * i
    print(f"{n} * {i} = {multiplicacao}")
    contador += 1

    if i != 0:
        divisao = n / i
        print(f"{n} / {i} = {divisao}")
        contador += 1

print(f"\nTotal de operações realizadas: {contador}")
