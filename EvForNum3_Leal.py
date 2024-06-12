#Evaluación Formativa N°3
#Jacquelinne Leal Mena

import os 
os.system("cls")

#Listas:

cargos = ["CEO","Desarrollador","Analista de datos"]


#Menú

while True:
    os.system("cls")
    print("""\tMenú\n
    1. Registrar trabajador
    2. Listar todos los trabajadores
    3. Imprimir plantilla de sueldos
    4. Salir del Programa""")

    while True:
        try:
            opc = int(input("Opción: "))
            if opc in(1,2,3,4):
                break
            else:
                print(">>> Opción inválida! Ingrese 1, 2, 3 o 4...")
        except:
            print(">>> Error! Debe ingresar un número!")
    
    if opc == 1:
        print("\tRegistro de Trabajador\n")
        
        while True:
            nom_ape = input("Ingrese nombre y apellido: ")
            if len(nom_ape) == 0:
                print("Error! Espacio en blanco!")
            else:
                break
        while True:
            cargo = input("Ingrese Cargo: ")
            if cargo not in(cargos):
                print("Error! El cargo ingresado NO está en los registros.. (CEO, Desarrollador, Analista de datos)")
            else:
                break
        while True:
            try:
                sueldo_br = int(input("Ingrese sueldo bruto: "))
                if sueldo_br < 0:
                    print("Valor inválido! Ha ingresado un número negativo!")
            except:
                print("Error! Debe ingresar un número mayor o igual a 0!")
    elif opc == 2:
        pass
    elif opc == 2:
        pass
    else:
        os.system("cls")
        print("Ha salido del Programa")
        break