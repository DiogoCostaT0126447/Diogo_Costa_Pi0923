n1, n2 = 1, 1
 
print("Construção da sequência de Fibonacci:\n")
 
for i in range(60):  
    print(" " * i + f"{n1} + {n2} = {n1 + n2}")  # Espaçamento em escada sem tabulação
    prox = n1 + n2  
    n1 = n2  
    n2 = prox  