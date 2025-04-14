"""
opc = 0

print("Bem vindo")
print("prima 1 para nome cliente")
print("prima 2 para Iban")
opc = input("Intrud opçao ")

match opc:
    case 1:
        print("Nome")
    case 2:
        print("Iban")
    case default:
        print("nao existe opc")
"""        
        
#entre 3 numero daber maior meio e menor

num1 = 3
num2 = 2
num3 = 1 

if num1>num2 and num2>num3:
    print("Numero 1 > 2 > 3")

elif num1>num3 and num3>num2:
    print("Numero 1 > 3 > 2 ")

elif num3>num2 and num2>num1:
    print("Numero 3 > 2 > 1 ")
    
elif num3>num1 and num1>num2:
    print("Numero 3 > 1 > 2 ")
    
elif num2>num1 and num1>num3:
    print("Numero 2 > 1 > 3")
    
else:
    print("Numero 2 > 3 > 1 ")