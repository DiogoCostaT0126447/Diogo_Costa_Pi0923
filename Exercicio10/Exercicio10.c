/*Ler 10 n�meros, e determinar o n�mero par e numero impar�.*/

#include <stdio.h>

int main() {
    int num, i;
    int pares[10], impares[10];
    int Pares = 0, Impares = 0;

    for (i = 0; i < 10; i++) {
        printf("Digite o %d� n�mero: ", i + 1);
        scanf("%d", &num);

        if (num % 2 == 0) {
            pares[Pares++] = num;
        } else {
            impares[Impares++] = num;
        }
    }

    printf("\nN�meros pares: ");
    for (i = 0; i < Pares; i++) {
        printf("%d ", pares[i]);
    }

    printf("\nN�meros �mpares: ");
    for (i = 0; i < Impares; i++) {
        printf("%d ", impares[i]);
    }

    return 0;
}

