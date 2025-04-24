def exibir_ascii():
    inicio = 0
    fim = 20

    while True:
        for i in range(inicio, fim):
            if i > 255:
                break
            print(f"Código ASCII: {i}, Caracter: {chr(i)}")

        resposta = input("\nDeseja continuar (S para sim, qualquer outra tecla para sair): ")

        if resposta != 'S':
            print("Saindo do programa.")
            break

        else:
            inicio += 20
            fim += 20


            if inicio > 255:
                print("Todos os códigos ASCII de 0 a 255 foram exibidos.")
                break
exibir_ascii()
