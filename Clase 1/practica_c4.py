def imprimir_global():
    print("imprimir valor de la variable global")
    print(msj) #mensaje global
    print("")

def saludar_2():
    msj="Bienvenidos al curso"
    print(msj) #mensaje saludar_2
    print("-------------------")

def modificar_saludo():
    global msj
    msj="Hello, welcome"
    print("se modificio el valor de la global") #mensaje saludar_3
    print("--------------------------")


#cuerpo principal
msj="Hola, bienvenido"
imprimir_global()
saludar_2()
modificar_saludo()
imprimir_global()