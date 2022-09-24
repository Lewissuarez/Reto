def areaRectangulo(ancho, largo):
    return ancho * largo 

def calcularPerimetro(ancho,largo):
    return ancho+ancho+largo+largo
    
ancho = int(input("Ingrese el ancho del rectangulo: "))
largo = int(input("Ingrese el largo del rectangulo: "))

print(calcularPerimetro(ancho, largo))
print(areaRectangulo(ancho, largo))

for i in range(0,largo):
    for j in range(0,ancho):
        print("*", end="")
    print()

