# --- Implementación de una Cola sin objetos ---

# Cola vacía
cola = []

# --- Funciones básicas ---
def esta_vacia(cola):
    return len(cola) == 0
#Verifica que la lista este vacia#

def encolar(cola, elemento):  # Enqueue
    cola.append(elemento)
    print(f"Se encoló: {elemento}")
#Agrega un elemento al final de la lista#

def desencolar(cola):  # Dequeue
    if not esta_vacia(cola):
        elemento = cola.pop(0)
        print(f"Se desencoló: {elemento}")
        return elemento
    else:
        print("La cola está vacía. No se puede desencolar.")
#Elimina el primer elemento de la lista#

def ver_frente(cola):  # Front
    if not esta_vacia(cola):
        print(f"Elemento al frente: {cola[0]}")
        return cola[0]
    else:
        print("La cola está vacía.")
#Muestra el primer elemento de la lista#

def mostrar_cola(cola):
    print("Estado actual de la cola:", cola)
#Muestra todos los elementos de la lista#

# --- Uso paso a paso ---
print("¿La cola está vacía?", esta_vacia(cola))
#Verifica que la lista este vacia#

encolar(cola, "Persona 1")
encolar(cola, "Persona 2")
encolar(cola, "Persona 3")
#Agrega 3 elementos a la lista#

mostrar_cola(cola)
ver_frente(cola)
#Muestra todo los elementos y el primer elemento de la lista#

desencolar(cola)
mostrar_cola(cola)
#Elimina el primer elemento y muestra la lista#

desencolar(cola)
desencolar(cola)
desencolar(cola)  # Intento extra
#Intenta eliminar 3 veces el primer elemento de la lista, el último intento marcara que la lista esta vacia#

print("¿La cola está vacía?", esta_vacia(cola))
#Verifica que la lista este vacia, devuelve True#
