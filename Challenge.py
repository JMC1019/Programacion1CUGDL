# Listas
lista_debiles = ["hola123", "contraseña", "cumpleaños", "123456", "abcdef", "qwertyl", "password"]
lista_numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lista_signosespeciales = ["?", "¿", "*", "+", "-", "_", "&", ":", ";", "#", "!", "@", "$", "%"]
lista_historial = []

# Variables globales
puntuacion_actual = 0
cantidadtotal = 0
contrasenasdebiles = 0
contrasenasseguras = 0

# Función opcion 1. Probar contraseña
def probar_contraseña():
    global cantidadtotal
    global contrasenasdebiles
    global contrasenasseguras
    global puntuacion_actual
    puntuacion_actual = 0

    print("\n***** Probador/Evaluador de Contraseñas *****")
    intento = input("Ingrese una contraseña: ")

    if intento.lower() in lista_debiles:
        contrasenasdebiles += 1
        cantidadtotal += 1
        print(f"\nContraseña encontrada en lista de contraseñas débiles")
    else:
        if len(intento) > 8:
            puntuacion_actual += 30
        if any(char in lista_numeros for char in intento):
            puntuacion_actual += 30
        if any(char in lista_signosespeciales for char in intento):
            puntuacion_actual += 40

        registro_historial = {
            "contraseña": intento,
            "puntaje": puntuacion_actual
        }

        lista_historial.append(registro_historial)
        contrasenasseguras += 1
        cantidadtotal += 1

        print("\nContraseña segura")
        print(f"Puntaje de seguridad: {puntuacion_actual}")

# Funcion opción 2. Ver contraseñas analizadas
def mostrar_contraseñas():
    print("\n***** Lista de contraseñas analizadas *****")
    if not lista_historial:
        print("El historial está vacío. Pruebe una contraseña primero.")
        return
    for registro in lista_historial:
        contraseña = registro["contraseña"]
        puntaje = registro["puntaje"]
        print(f"Contraseña: {contraseña} | Puntaje: {puntaje}")

# Función opción 3. Mostrar estadísticas
def mostrar_estadísticas():
    print("\n***** Estadísticas de Análisis *****")
    print(f"Cantidad de contraseñas analizadas: {cantidadtotal}")
    print(f"Cantidad de contraseñas débiles: {contrasenasdebiles}")
    print(f"Cantidad de contraseñas seguras: {contrasenasseguras}")

# Funcion mensaje tipo hacker
def saludo(nombre):
    print(f"\nConexion al sistema autorizada Bienvenido 0111010101-{nombre}-001100110")

# Inicio
nombre = input("Ingresa tu nombre de usuario: ")
saludo(nombre)

# Menú principal - Ciclo while
while True:
    print("\n***** Menú principal *****")
    print("1. Probar una contraseña")
    print("2. Ver contraseñas analizadas")
    print("3. Mostrar estadísiticas")
    print("4. Salir")
    opcion = input("Elije una opcion (ejemplo 1): ")
    if opcion == "1":
        probar_contraseña()
    elif opcion == "2":
        mostrar_contraseñas()
    elif opcion == "3":
        mostrar_estadísticas()
    elif opcion == "4":
        break
    else:
        print("\nOpción inválida")

# Despedida
print("\nFin de la conexion")