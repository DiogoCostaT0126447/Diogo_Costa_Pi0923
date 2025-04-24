print("multiplos de 5 mas não múltiplos de 3")
for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(i)
