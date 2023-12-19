import os

alumnos = []
isActive = True
porcentajeNotas = (0.6,0.15,0.25)
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar un estudiante\n4. Mostrar notas\n5. Salir\nSeleccione una opcion: "
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu = 0
while(isActive):
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
    else:
        os.system("cls")
        if(opMenu == 1):
            rta = "S"
            while(rta in ["S","s"]):
                codigoEstudiante = input("Ingrese el codigo del estudiante: ")
                nobmreEstudiante = input("Ingrese el nombre del estudiante: ")
                edadEstudiante = int(input(f"Ingrese la edad del estudiante {nobmreEstudiante}: "))
                estudiante = [codigoEstudiante,nobmreEstudiante,edadEstudiante,[],[],[]]
                alumnos.append(estudiante)
                print(estudiante)
                rta = input("¿Desea registrar otro alumno? S(si) o N(no)")
                os.system("cls")

        elif(opMenu == 2):
            
            opNotas = 0
            isActiveGrade = True
            while(isActiveGrade):

                for i, item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                
                try:
                    opNotas = int(input("Seleccione una opcion: "))

                except ValueError:
                    print("Error en el dato ingresado")

                else:
                    if (opNotas in [1,2,3]):
                        if(len(alumnos) > 0):
                            otroEstudiante = "S"
                            while(otroEstudiante in ["s","S"]):
                                codigoEstudiante = input("Ingrese el codigo del estudiante: ")
                                rta = "S"
                                while(rta in ["S","s"]):
                                    if(opNotas == 1):
                                        nota = float(input("Ingrese la nota del parcial: "))
                                    elif(opNotas == 2):
                                        nota = float(input("Ingrese la nota del quiz: "))
                                    elif(opNotas == 3):
                                        nota = float(input("Ingrese la nota del trabajo: "))

                                    for item in alumnos:
                                        if codigoEstudiante in item:
                                            if opNotas == 1:
                                                item[3].append(nota)
                                                print(item)
                                            elif opNotas == 2:
                                                item[4].append(nota)
                                                print(item)
                                            else:
                                                item[5].append(nota)
                                                print(item)
                                        else:
                                            print(f"El estudiante con codigo {codigoEstudiante} no existe")
                                            break
                                    rta = input("¿Desea registrar otra nota? S(si) o N(no)")
                                otroEstudiante = input("¿Desea ingresar la nota de otro estudiante? S(si) o N(no)")
                        else:
                            print("Ingrese una opcion valida")
                            pause = input("Presione enter para continuar...")
                            os.system("cls")
                    elif(opNotas == 4):
                            isActiveGrade = False
                    else:
                        print("ERROR: Debe haber almenos un(1) estudiante registrado")
                        input("")

        elif(opMenu == 3):
            codigo = input("Ingrese el codigo del estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)
            input("Presione enter para continuear...")


        elif(opMenu == 4):
            mostrarNotas = []
            totalNotas = [0,0,0]
            promedio = 0.0
            for item in alumnos:
                for index, datosAlumno in enumerate(item):
                    if (type(datosAlumno) == list):
                        if(len(datosAlumno) > 0):
                            for cadaNota in datosAlumno:
                                promedio += cadaNota
                            if(index == 3):
                                totalNotas[0] = format(((promedio/len(datosAlumno)) * porcentajeNotas[0]),".2f")
                            elif(index == 4):
                                totalNotas[1] = format((promedio/len(datosAlumno)) * porcentajeNotas[1],".2f")
                            else:
                                totalNotas[2] = format((promedio/len(datosAlumno)) * porcentajeNotas[2],".2f")

                if (totalNotas != [0,0,0]):
                    alumnoResume = {
                            "Nombre         " : item[1],
                            "Notas Parciales" : item[3],
                            "Total Parciales" : totalNotas[0],
                            "Notas Quices   " : item[4],
                            "Total Quices   " : totalNotas[1],
                            "Notas Trabajos " : item[5],
                            "Total Trabajos " : totalNotas[2]
                            }
                    mostrarNotas.append(alumnoResume)
                    for elementos in mostrarNotas:
                        if type(elementos) == dict:
                            for key, valor in elementos.items():
                                print(f"{key} ____ {valor}.")
                    input("")
                else:
                    print("No se encuentran notas")
                    input("Presione enter para continuar...")
        elif(opMenu == 5):
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            print("Opcion invalida")
    
    