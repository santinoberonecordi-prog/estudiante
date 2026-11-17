def crear_estudiante(legajo, nombre, curso):

    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "curso": curso,
        "notas": [],
        "materias": []
    }

    print("ESTUDIANTE CREADO CORRECTAMENTE")
    print("Legajo:", legajo)
    print("Nombre:", nombre)
    print("Curso:", curso)

    return estudiante


def listar_estudiantes(lista):

    if len(lista) == 0:
        print("No hay estudiantes registrados")

    else:
        for estudiante in lista:
            mostrar_diccionario(estudiante)
            print("------------------------")


def listar_nombres(lista):

    if len(lista) == 0:
        print("No hay estudiantes registrados")

    else:
        for i in range(len(lista)):
            print("ID:", i, "-", lista[i]["nombre"])


def mostrar_diccionario(dic):

    print("Legajo:", dic["legajo"])
    print("Nombre:", dic["nombre"])
    print("Curso:", dic["curso"])

    print("Notas:")

    if len(dic["notas"]) == 0:
        print("No tiene notas registradas")
    else:
        for nota in dic["notas"]:
            print(nota)

    print("Materias:")

    if len(dic["materias"]) == 0:
        print("No tiene materias registradas")
    else:
        for materia in dic["materias"]:
            print(materia)


def calcularPromedioLista(lista):

    if len(lista) == 0:
        print("No hay notas registradas para calcular el promedio")
        return 0

    suma = 0
    contador = 0

    for nota in lista:
        suma = suma + nota
        contador = contador + 1

    promedio = suma / contador

    return promedio
