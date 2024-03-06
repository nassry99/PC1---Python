#Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
#entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
#Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
#hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
#Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
#suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
#las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar

#Solicitar la hora ingresada 
hora=input("Por favor ingrese la hora en formato de 24: ")

#extraer hora
hora_split=hora.split(":")
hora_ingresada=int(hora_split[0])
minutos_ingresado=int(hora_split[1])

#verificar hora 
if 7<=hora_ingresada < 8 :
    print("Hora de desayunar")
elif 12<= hora_ingresada < 13 :
    print("Es hora de almorzar")
elif 18<= hora_ingresada < 19 :
    print("Es hora de cenar")
else:
    print("Ingrese una opcion valida")