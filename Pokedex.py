continuar="si"
lista_global = []

def agregar_pokemon(nombre, tipo, nivel):
    pokemon = {
        'nombre': nombre,
        'tipo': tipo,
        'nivel': nivel
    }
    lista_global.append(pokemon)

def mostrar_pokemones():
    print("\n**** Lista de Pokemones ****")
    for pokemon in lista_global:
        print(f"Nombre: {pokemon['nombre']}, Tipo: {pokemon['tipo']}, Nivel: {pokemon['nivel']}")

def elimimar_pokemon(nombre):
    for pokemon in lista_global:
        if pokemon['nombre'] == nombre:
            lista_global.remove(pokemon)
            print(f"Pokemon {nombre} eliminado de la Pokedex")
        else:
            print("No se encontro el poquemon")

while continuar == "si":
    print("\n**** Menu Pokedex ****"
          "\n1. Agregar Pokemon"
          "\n2. Borrar Pokemon"
          "\n3. Consultar Pokedex"
          "\n4. Salir")
    opcion=input("Ingresa una opcion (ejemplo: 1): ")
    if opcion=="1":
        nombre = input("\nIngrese el nombre del pokemon: ")
        tipo = input("Ingrese el tipo del pokemon: ")
        nivel = int(input("Ingrese el nivel del pokemon: "))
        agregar_pokemon(nombre, tipo, nivel)
        print(f"\nPokemon {nombre} agregado a la Pokedex")
    elif opcion=="2":
        nombre = input("\nIngrese el nombre del pokemon a eliminar: ")
        elimimar_pokemon(nombre)
    elif opcion=="3":
        mostrar_pokemones()
    elif opcion=="4":
        continuar="no"
    else:
        print("\nOpcion no valida")

print("\nGracias por usar la Pokedex")