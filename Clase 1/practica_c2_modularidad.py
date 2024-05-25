def saludar():
    nombre=input("Como te llamas?/n")
    print(f"Hola {nombre}")

def calcular():
    n1=int(input("Cual fue la nota 1/n"))
    n2=int(input("Cual fue la nota 2/n"))
    n3=int(input("Cual fue la nota 3/n"))
    prom=(n1+n2+n3)/3
    print(f"El promedio es {prom}")

#modulo para despedirse de forma no personalizada
def despedirse():
    print("Hasta luego!")

#cuerpo principal
saludar()
calcular()
despedirse()
