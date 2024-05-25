def saludar():
    global nombre, apellido
    nombre=input("Como te llamas?/n")
    apellido=input("Cual es tu apellido?/n")
    print(f"Hola {nombre} {apellido}")

def calcular():
    global promedio
    n1=int(input(f"Cual fue la nota 1/n {nombre} {apellido}"))
    n2=int(input("Cual fue la nota 2/n"))
    n3=int(input("Cual fue la nota 3/n"))
    promedio=(n1+n2+n3)/3
    print(f"El promedio es {promedio}")

#modulo para despedirse de forma no personalizada
def despedirse():
    print(f"Hasta luego! {nombre} {apellido}" )
    if promedio>15:
        print("Has aprobado, felicidades")
    else:
        print("Has reprobado, sigue estudiando")

#cuerpo principal
nombre=""
apellido=""
promedio=0
n1=0
n2=0
n3=0
saludar()
calcular()
despedirse()
