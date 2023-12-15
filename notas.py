import os

alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2.Registrar Nota\n3.Salir\nSeleccione una opcion: "
subMenuNotas = ["Pariales","Quices","Trabajos","Regresar al menu principal"]
opMenu = 0
while(isActive):
    os.system("clear")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
    else:
        if(opMenu == 1):
            pass
        elif(opMenu == 2):
            
            opNotas = 0
            isActiveGrade = True
            while(isActiveGrade):

                for i, item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                
                try:
                    opNotas = int(input(":"))
                except ValueError:
                    print("Error en el dato ingresado")
                else:
                    if(opMenu == 1):
                        pass
                    elif(opMenu == 2):
                        pass
                    elif(opMenu == 3):
                        pass
                    elif(opMenu == 4):
                        pass
                    else:
                        pass
                pass

        elif(opMenu == 3):
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            print("Opcion invalida")
    
    os.system("wait")

