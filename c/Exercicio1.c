#include <stdio.h>

// Desenvolva um programa que assuma uma entrada em Segundos e transforme em Horas, Minutos e Segundos.

int main() {
    int segundos = 0;
    int minutos = 0;
    
    horas = segundos / 3600;
    segundos %= 3600;
    minutos = segundos / 60;
    segundos %= 60;
    
    printf("Insira o tempo em segundos: ");
    scanf("%d", &segundos);
    printf("O numero inserido equivale a %d Horas, %d Minutos e %d Segundos.\n", horas, minutos, segundos);

    return 0;
}

