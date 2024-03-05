#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

#solcitar la edad del cliente
N=int(input("solicitar la edad del cliente: "))
#Hacer la condicion
if N<4:
    #mostror la resolucion
    print("puede entrar gratis")
elif N>=4 and N<18:
    print("Usted debe pagar 5$")
elif N>=18:
    print("Usted debe pagar 10$")