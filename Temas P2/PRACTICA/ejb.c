/*B)

Escribir una función en C que reciba por parámetro un vector de 
enteros positivos y su longitud, y devuelva la cantidad de valores 
que son múltiplos del elemento siguiente.

Ejemplo:


[16, 8, 2, 4, 5, 15] ---> 3, 
porque 16 es múltiplo de 8; 8 lo es de 2 y 5, de 15.


Escribir un programa que invoque dicha función 
pasando como parámetro el arreglo del ejemplo y su longitud. */

int contarMultiplos(int vec[], int n) {
    if (n <= 1) {
        return 0;
    }
        
    // Verificar si vec[1] es múltiplo de vec[0]
    if (vec[0] % vec[1] == 0) {
        return 1 + contarMultiplos(vec + 1, n - 1);
    }
    
    else{
        return  contarMultiplos(vec + 1, n - 1);
    }
}