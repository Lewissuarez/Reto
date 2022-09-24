def areaRectangulo(ancho, largo):
    return ancho * largo 

def calcularPerimetro(ancho,largo):
    return ancho+ancho+largo+largo

ancho = input(int("Ingrese el ancho del rectangulo: "))
largo = input(int("Ingrese el largo del rectangulo: "))

areaRectangulo(ancho, largo)
calcularPerimetro(ancho, largo)

