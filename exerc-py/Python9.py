
while True:
    num = int(input("Digite um número entre 1 e 100: "))
    
    if 1 <= num <= 100:
        print(f"Você digitou um número válido: {num}")
        break 
    else:
        print("Número inválido! Tente novamente.")

