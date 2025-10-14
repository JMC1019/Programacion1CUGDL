alumnos = []
continuar = 1

def agregar_alumno(nombre, edad, carrera):
    alumno = {
        'nombre': nombre,
        'edad': edad,
        'carrera': carrera
    }
    alumnos.append(alumno)
    return

while continuar <=3:
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    carrera = input("Ingrese la carrera del alumno: ")
    agregar_alumno(nombre, edad, carrera)
    continuar += 1

print(alumnos)