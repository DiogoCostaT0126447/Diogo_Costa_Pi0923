num = int(input("Digite um número: "))

print(f"\nTabuada de {num}:")

for i in range(1, 11):  
    resul = num * i
    print(f"{num} x {i} = {resul}")
