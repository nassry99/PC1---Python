#Problema 2:
#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.#

#solicitar al cliente el monto final del restaurante
monto=float(input("Señale el monto final: "))
#porcentaje de propina 
propina=float(input("Introduzca el porcentaje:"))
#calular el monto de la propina
calcpropina=monto*(propina/100)
#Mencionar los montos finales 
final=monto+calcpropina
#
print("Su monto final sera", final ,"Gracias por el consumo")
