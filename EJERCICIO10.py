#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']
#definir lista 
listaoriginal=['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#eliminar items
eliminar_items=[0, 4 , 5]
#Ordenar las posiciones
eliminar_items.sort(reverse=True)

# Eliminar los elementos en las posiciones especificadas usando pop()
for pos in eliminar_items:
    listaoriginal.pop(pos)

# Mostrar la lista después de la eliminación
print(listaoriginal)