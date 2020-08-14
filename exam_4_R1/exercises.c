/*
Consigna:
    Escribir en C una función que pida al usuario que ingrese un número natural e imprima por pantalla los primeros n números primos. 
    Se debe implementar una función auxiliar es_primo que recibe un número y devuelve true o false dependiendo de si el número es primo o no. 
    Por ejemplo, si el usuario ingresa 4, debe imprimir 2,3,5,7. Nota: incluir stdbool.h para poder utilizar el tipo bool.
*/


#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define BUFFERSIZE 10

bool es_primo(int n) {
    bool flag = true;
    for (int x = n-1; n > 1; x--) {
        if (n % x == 0) {
            flag = false;
            break;
        }
    }
    return flag;
 }


int main(int n) {
    char buffer[BUFFERSIZE];
    printf("Ingrese un número a buscar (hasta 5 cifras): ");
    fgets(buffer, BUFFERSIZE, stdin);
    int num = atoi(buffer);

    for(int x = 0; x < n; x++) {
        if (es_primo(x)) { 
            printf("%d ", x);
        }
    }
}
