# --- Implementación de una Pila sin objetos ---

# Pila vacía
pila = []

# --- Funciones básicas ---
def esta_vacia(pila):
    return len(pila) == 0
#Verifica que la lista este vacia#

def apilar(pila, elemento):  # Push
    pila.append(elemento)
    print(f"Se apiló: {elemento}")
#Agrega un elemento a la lista#

def desapilar(pila):  # Pop
    if not esta_vacia(pila):
        elemento = pila.pop()
        print(f"Se desapiló: {elemento}")
        return elemento
    else:
        print("La pila está vacía. No se puede desapilar.")
#Elimina el ultimo elemento de la lista#

def ver_tope(pila):  # Peek
    if not esta_vacia(pila):
        print(f"Elemento en el tope: {pila[-1]}")
        return pila[-1]
    else:
        print("La pila está vacía.")
#Muestra el ultimo elemento de la lista#

def mostrar_pila(pila):
    print("Estado actual de la pila:", pila)
#Muestra todos los elementos de la lista#


# --- Uso paso a paso ---
print("¿La pila está vacía?", esta_vacia(pila))

apilar(pila, "Plato 1")
apilar(pila, "Plato 2")
apilar(pila, "Plato 3")
#Agrega 3 elementos a la lista#

mostrar_pila(pila)
ver_tope(pila)
#Muestra todo los elementos y el ultimo elemento de la lista#

desapilar(pila)
mostrar_pila(pila)
#Elimina el ultimo elemento y muestra la lista#

desapilar(pila)
desapilar(pila)
desapilar(pila)  # Intento extra
#Intenta eliminar 3 veces el ultimo elemento de la lista, el último intento marcara que la lista esta vacia#

print("¿La pila está vacía?", esta_vacia(pila))
#Verifica que la lista este vacia, devuelve True#