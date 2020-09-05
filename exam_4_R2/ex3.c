/*
Consigna: Implementar en C la función potencia(), que recibe la base (número entero) y el exponente (número entero no negativo) 
    y devuelva el resultado de elevar la base al exponente. 
    Nota: no pueden incluir bibliotecas para resolver la potencia, por lo que la funcion pow no está disponible para usar.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define BUFFERSIZE 10

int potencia(int base, int exp) {
    if(exp == 1) {
        return base;
    } 
    return base * potencia(base, exp-1);
}


int main() {
    char buffer[BUFFERSIZE];
    printf("Ingrese la base: ");
    fgets(buffer, BUFFERSIZE, stdin);
    int base = atoi(buffer);
    printf("Ingrese el exponente: ");
    fgets(buffer, BUFFERSIZE, stdin);
    int exp = atoi(buffer);
    int result = potencia(base, exp);
    printf("El resultado de la potencia es: " + result);
}


