"""
opc=0
 
print("Bem Vindo" )
print("Prima 1 para nome cliente")
print("Prima 2 para Iban")
opc = input("Introduza a opção")
 
match opc:
    case 1:
        print("Nome")
    case 2:
        print("Iban")
    case default:
        print("Falhou opção")
 
if opc == 1:
    print("Nome")
elif opc == 2:
    print("Iban")
else:
    print("Não existe essa opção")
"""
#Entre 3 numeros saber qual e o maior, meio e menor
 
num1 = 1
num2 = 2
num3 = 3

 
if num1>num2 and num2>num3:
    print("Numero 1 > 2 > 3 ")
elif num1>num3 and num3>num2:
    print("Numero 1 > 3 > 2 ")
elif num3>num2 and num2>num1:
    print("Numero 3 > 2 > 1 ")
elif num3>num1 and num1>num2:
    print("Numero 3 > 1 > 2 ")
elif num2>num1 and num1>num3:
    print("Numero 2 > 1 > 3 ")
else:
    print("Numero 2 > 3 > 1 ")