contador = 0    
num = 2         

print("Os 10 primeiros números primos são:")

while contador < 10:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num)
        contador += 1

    num += 1
