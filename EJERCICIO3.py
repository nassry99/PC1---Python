#Problema 3:
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.

#pesos 
peso_paya=112
peso_muñe=75
#numeros de muñecos y payasos solicitados 
cant_payasos=int(input("Ingrese la cantidad de payasos: "))
cant_muñe=int(input("Ingrese la cantidad de muñecas: "))
#calcular el peso de la caja 
peso_total=(peso_paya*cant_payasos)+(peso_muñe*cant_muñe)
#peso total 
print("El peso final es de",peso_total, "g gracias por su compra, espere su paquete.")