"""2. Escribir un programa que solicite el ingreso de una serie de números.
Por cada número ingresado se deberá informar si el mismo es ó no, un número
capicúa.
Se debe evaluar que lo ingresado, sea un número entero positivo; de lo contrario,
se debe enviar el mensaje “Número Inválido”, y solicitar el siguiente.
El ingreso de números, termina cuando en lugar de un número, el usuario ingresa
“FIN”."""

num = 0 

while (num != "FIN"):
        num = input("ingrese un numero o FIN para salir: ")
        print(f"{num}")

        if num != "FIN":

             if (int(num) <= 0 or not num.isdigit()):
                print("Numero invalido")
             else: 
                numInvertido = num[::-1]

                if num == numInvertido:
                    print("es capicua")
                else:
                    print("no es capicua")

           