




# Función para mostrar el menú
def mostrar_menu():
    print("Elija una opción:")
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta de los dos números (el primero menos el segundo)")
    print("3. Mostrar multiplicación de los dos números")

# Función para realizar la suma
def suma(num1, num2):
    return num1 + num2

# Función para realizar la resta
def resta(num1, num2):
    return num1 - num2

# Función para realizar la multiplicación
def multiplicacion(num1, num2):
    return num1 * num2

# Leer dos números ingresados por el usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú
mostrar_menu()

# Leer la opción seleccionada por el usuario
opcion = input("Ingrese el número de opción deseada: ")

# Realizar la operación correspondiente según la opción seleccionada
if opcion == '1':
    print("La suma de los dos números es:", suma(num1, num2))
elif opcion == '2':
    print("La resta de los dos números es:", resta(num1, num2))
elif opcion == '3':
    print("La multiplicación de los dos números es:", multiplicacion(num1, num2))
else:
    print("Opción inválida. Por favor, elija una opción válida.")
