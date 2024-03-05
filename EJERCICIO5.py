#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

#solcitar el numero 
N_shows=int(input("solicitar el numero de show vistos: "))
#Hacer la condicion de 3 shows
shows_vistos=N_shows>3
#mostrar los shows vistos
print("¿Ha visto más de 3 shows musicales en el último año?:", shows_vistos)