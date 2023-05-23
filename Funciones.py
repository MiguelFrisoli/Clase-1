#1

def primos(x):
    
    for numero in range (x, 3, -1):
        
        for divisor in range (2, numero):

            operacion1 = numero % divisor
            operacion2 = numero / divisor

            if operacion1 != 0 and operacion2 == 1:
                print (numero, end= " ")

x = int (input())
primos (x)

#2

def primos(x):
    for i in range (2, x+1):
        divisor = 2

        while i % divisor != 0:
            divisor +=1
            if divisor == i:
                print (i, end= " ")

numero= int(input("Ingrese un numero positivo y entero"))
x = numero
primos (x)

#3

def fibonacci(x):
    n_antepenultimo = 0
    n_penultimo = 1
    n_ultimo = 0
    for i in range (numero_D_veces):
   
        n_ultimo = n_penultimo + n_antepenultimo
        
        n_antepenultimo = n_penultimo
        n_penultimo = n_ultimo
        print (n_ultimo, end= " ")

numero_D_veces = int(input("ingrese el numero de la serie de Fibonacci que quiere conocer: "))
x = numero_D_veces
fibonacci (numero_D_veces)

#4

primer_numero = float(input("ingrese un numero"))
segundo_numero = float(input("ingrese otro numero"))

operacion_elegida = input("Ingrese el numero que representa la operación que quiere realizar, siendo estos: 1 para suma; 2 para resta; 3 para multiplicacion; 4 para division; 5 para potencia o 6 para division entera")

if operacion_elegida != "1" or "2" or "3" or "4" or "5" or "6":
    operacion_elegida = input("Has elegido una opcion incorrecta, ingresa nuevamente la operacion que deseas realizar, siendo: 1 para suma; 2 para resta; 3 para multiplicacion; 4 para division; 5 para potencia o 6 para division entera")

operaciones = {
"1": primer_numero + segundo_numero,
"2": primer_numero - segundo_numero,
"3": primer_numero * segundo_numero,
"4": primer_numero / segundo_numero,
"5": primer_numero ** segundo_numero,
"6": primer_numero // segundo_numero}

print("El resultado de la operacion elegida es:", operaciones [operacion_elegida])


#5

numero = float(input("Ingrese el numero que quiera convertir: "))
operacion_elegida = input("Elige la operación que prefieras, ingresando: kilometro_a_milla o milla_a_kilometro o centimetro_a_pulgada o pulgada_a_centimetro o gramo_a_libra o libra_a_gramo")
if operacion_elegida != "kilometro_a_milla" or "milla_a_kilometro" or "centimetro_a_pulgada" or "pulgada_a_centimetro" or "gramo_a_libra" or "libra_a_gramo":
    operacion_elegida = input("Has escrito incorrectamente la operación elegida, vuelve a intentarlo, elige entre las siguientes operaciones: kilometro_a_milla o milla_a_kilometro o centimetro_a_pulgada o pulgada_a_centimetro o gramo_a_libra o libra_a_gramo")
operaciones = {
"kilometro_a_milla" : numero * 1.60934,
"milla_a_kilometro" : numero / 1.60934,
"centimetro_a_pulgada" : numero * 0.393701,
"pulgada_a_centimetro" : numero / 0.393701,
"gramo_a_libra" : numero * 0.00220462,
"libra_a_gramo" : numero / 0.00220462}

print(numero, "convertido de ", operacion_elegida, "es:", operaciones [operacion_elegida])