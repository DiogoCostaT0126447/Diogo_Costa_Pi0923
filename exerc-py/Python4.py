num = int(input(f"Insira o numero: "))
primo = True
for i in range(2, num):
    if num % i == 0 or i == 1:
        primo = False
        break
if primo:
    print(f"o num {num} é num primo")
else:
    print(f"o num {num} NAO é num primo")
