#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta N. 

#solcitar el numero 
N=int(input("solicitar el numero entero positivo: "))
#Hacer la condicion
if N>=0:
    Suma=N*(N+1)/2
    #mostror la resolucion
    print("la suma de numero consecutivos enteros positivos hasta",N,"es",Suma,"total")
else:
    print("Ponga un numero positivo entero")
