
def inicio():

    print("\n" + '*'*31 + '\n' + '*'*9 + ' Curso Ideal '  + '*'*9 + '\n' + '*'*31)
    id = input("\nIngrese Id: ")
    nombre = input("Ingrese su nombre: ")
    

    terminar = False

    while not terminar:

        materia = input("\nIngrese Materia que desea Verificar: ")

        if materia == "calculo integral" or materia == "Mecanica y laboratorio" or materia == "matematica financiera":
            terminar = True
        else:
            print("Materia Invalida")

    terminar = False

    while not terminar:

        ubicacion = input("\nIngrese municipio de residencia: ")

        if ubicacion == "bucaramanga" or ubicacion == "piedecuesta" or ubicacion == "giron" or ubicacion == "floridablanca":
            terminar = True
        else:
            print("Ubicación Inválida")



    print(f"\nSeñor@ {nombre} la mejor sede para recibir tu clase es: \nclase en el CCU")

    terminar = False

    while not terminar:

        busqueda = input(f"Señor@ {nombre} ¿Deseas averiguar acerca de otra materia?(si/no): ")

        if busqueda == "si":

            terminar = False

            materia = input("\nIngrese Materia que desea Verificar: ")

            if materia == "calculo integral" or materia == "Mecanica y laboratorio" or materia == "matematica financiera":
                print(f"\nSeñor@ {nombre} la mejor sede para recibir tu clase es: \nclase en el CCU")
            else:
                print("Materia Invalida\n")

        elif busqueda == "no":
            terminar = True
            

    
        

print(inicio())