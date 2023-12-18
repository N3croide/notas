import os

alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar un estudiante\n4. Salir\nSeleccione una opcion: "
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu = 0
while(isActive):
    os.system("clear")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
    else:
        os.system("clear")
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
                os.system("clear")

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
                        elif(opNotas == 4):
                            isActiveGrade = False
                        else:
                            print("Ingrese una opcion valida")
                            pause = input("Presione enter para continuar...")
                            os.system("clear")
                    else:
                        print("ERROR: Debe haber almenos un(1) estudiante registrado")
                        input("")

        elif(opMenu == 3):
            codigo = input("Ingrese el codigo del estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)


        elif(opMenu == 4):
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            print("Opcion invalida")
    
    os.system("wait")