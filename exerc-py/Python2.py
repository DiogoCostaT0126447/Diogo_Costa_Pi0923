for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é ÍMPAR.")