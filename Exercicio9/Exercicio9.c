/*Ler para uma variável INTEIRA um número de 1 a 12 e mostrar o nome do mês correspondente.
 Caso o mês não existir, mostrar essa informação.*/

 #include <stdio.h>

 int main(){
 int nmr;

 printf("Insira um numero que vai corresponder a um mes: ");
 scanf("%d", &nmr);
 printf("\n");

 if(nmr == 1){
    printf( "NMR inserido equivale a janeiro");
 }

 else if(nmr == 2){
    printf( "NMR inserido equivale a fevereiro");
 }

 else if(nmr == 3){
    printf( "NMR inserido equivale a marco");
 }

 else if(nmr == 4){
    printf( "NMR inserido equivale a abril");
 }

 else if(nmr == 5){
    printf( "NMR inserido equivale a maio");
 }

 else if(nmr == 6){
    printf( "NMR inserido equivale a junho");
 }

 else if(nmr == 7){
    printf( "NMR inserido equivale a julho");
 }

 else if(nmr == 8){
    printf( "NMR inserido equivale a agosto");
 }

 else if(nmr == 9){
    printf( "NMR inserido equivale a setembro");
 }

 else if(nmr == 10){
    printf( "NMR inserido equivale a outubro");
 }

 else if(nmr == 11){
    printf( "NMR inserido equivale a novembro");
 }

 else if(nmr == 12){
    printf( "NMR inserido equivale a dezembro");
 }

 else{
    printf("Numero invalido");
 }


 }
