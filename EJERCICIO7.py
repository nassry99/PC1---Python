#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

# Función para mostrar el menú
def mostrar_menu():
    print("Elija una opción:")
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta de los dos números (el primero menos el segundo)")
    print("3. Mostrar multiplicación de los dos números")

# Función para realizar la suma
def suma(a, b):
    return a+b

# Función para realizar la resta
def resta(a, b):
    return a-b

# Función para realizar la multiplicación
def multiplicacion(a, b):
    return a*b

# Leer dos números ingresados por el usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Mostrar el menú
mostrar_menu()

# Leer la opción seleccionada por el usuario
opcion = input("Ingrese el número de opción deseada: ")

# Realizar la operación correspondiente según la opción seleccionada
if opcion == '1':
    print("La suma de los dos números es:", suma(a, b))
elif opcion == '2':
    print("La resta de los dos números es:", resta(a, b))
elif opcion == '3':
    print("La multiplicación de los dos números es:", multiplicacion(a, b))
else:
    print("Opción inválida. Por favor, elija una opción válida.")
