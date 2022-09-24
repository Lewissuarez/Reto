def areaRectangulo(ancho, largo):
    return ancho * largo 

ancho = int(input("Ingrese el ancho del rectangulo: "))
largo = int(input("Ingrese el largo del rectangulo: "))

print(areaRectangulo(ancho, largo))

for i in range(0,largo):
    for j in range(0,ancho):
        print("*", end="")
    print()