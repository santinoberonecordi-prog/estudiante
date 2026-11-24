from estudiante import *


def mostrar_menu():

    print()
    print("========= SISTEMA DE GESTION ESCOLAR =========")
    print("1) Crear estudiante")
    print("2) Listar estudiantes")
    print("3) Ingresar nota a un estudiante")
    print("4) Calcular promedio individual")
    print("5) Agregar materia a estudiante")
    print("6) Mostrar materias cursadas")
    print("7) Salir")
    print("==============================================")



def main():

    lista_bd = []

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":

            nombre = input("Ingrese el nombre del estudiante: ")
            curso = input("Ingrese el curso: ")

            legajo = len(lista_bd) + 10000

            nuevo = crear_estudiante(legajo, nombre, curso)

            lista_bd.append(nuevo)


        elif opcion == "2":

            listar_estudiantes(lista_bd)


        elif opcion == "3":

            if len(lista_bd) == 0:
                print("No hay estudiantes registrados")

            else:

                listar_nombres(lista_bd)

                try:
                    id = int(input("Ingrese el ID del estudiante: "))

                    if id >= 0 and id < len(lista_bd):

                        nota = float(input("Ingrese la nota: "))

                        if nota >= 0 and nota <= 10:

                            lista_bd[id]["notas"].append(nota)

                            print("Nota agregada correctamente")

                        else:
                            print("La nota debe estar entre 0 y 10")

                    else:
                        print("ID incorrecto")

                except ValueError:
                    print("Ingrese un numero valido")


        elif opcion == "4":

            if len(lista_bd) == 0:
                print("No hay estudiantes registrados")

            else:

                listar_nombres(lista_bd)

                try:
                    id = int(input("Ingrese el ID del estudiante: "))

                    if id >= 0 and id < len(lista_bd):

                        promedio = calcularPromedioLista(
                            lista_bd[id]["notas"]
                        )

                        if len(lista_bd[id]["notas"]) > 0:
                            print(
                                "El promedio de",
                                lista_bd[id]["nombre"],
                                "es:",
                                round(promedio, 2)
                            )

                    else:
                        print("ID incorrecto")

                except ValueError:
                    print("Ingrese un numero valido")


        elif opcion == "5":

            if len(lista_bd) == 0:
                print("No hay estudiantes registrados")

            else:

                listar_nombres(lista_bd)

                try:
                    id = int(input("Ingrese el ID del estudiante: "))

                    if id >= 0 and id < len(lista_bd):

                        materia = input("Ingrese el nombre de la materia: ")

                        if materia.strip() != "":

                            lista_bd[id]["materias"].append(materia)

                            print("Materia agregada correctamente")

                        else:
                            print("El nombre de la materia no puede estar vacio")

                    else:
                        print("ID incorrecto")

                except ValueError:
                    print("Ingrese un numero valido")


        elif opcion == "6":

            if len(lista_bd) == 0:
                print("No hay estudiantes registrados")

            else:

                listar_nombres(lista_bd)

                try:
                    id = int(input("Ingrese el ID del estudiante: "))

                    if id >= 0 and id < len(lista_bd):

                        print(
                            "Materias de:",
                            lista_bd[id]["nombre"]
                        )

                        if len(lista_bd[id]["materias"]) == 0:
                            print("No tiene materias registradas")

                        else:
                            for materia in lista_bd[id]["materias"]:
                                print("-", materia)

                    else:
                        print("ID incorrecto")

                except ValueError:
                    print("Ingrese un numero valido")

        elif opcion == "7":

            print("Programa finalizado")
            break

        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()
