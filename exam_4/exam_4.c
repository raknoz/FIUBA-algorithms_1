/*
    1. Escribir una función en C que reciba un arreglo de enteros, su largo, y un número y devuelva la cantidad de veces que 
    aparece ese número en el arreglo. Mostrar su correcto funcionamiento escribiendo un programa (un main) que permita probarla 
    pidiéndole un entero al usuario para buscar en un arreglo predefinido.
*/
#include <stdio.h>
#include <string.h>

#define BUFFERSIZE 10

int contadorNumero(int buscado, int len_array, int* lista) {
    //Función que cuenta cuantos ocurrencias hay del número buscado en la lista que se le pasa por parámetro.
    int contador = 0;
    for(int x= 0; x < len_array; x++) {
        if (lista[x] == buscado) {
            contador+=1;
        }
    }
    return contador;
}

int main() {
    //Le pido al usuario que ingrese en número que sea buscar.
    int arreglo[15] = {1,2,3,4,6,7,8,9,0,23,54,69,123,90, 45};
    char buffer[BUFFERSIZE];
    printf("Ingrese un número a buscar (hasta 5 cifras): ");
    fgets(buffer, BUFFERSIZE, stdin);
    int num = atoi(buffer);
    int contador = contadorNumero(num, sizeof(arreglo), arreglo);
    printf("El número %d aparece %s veces");
}

