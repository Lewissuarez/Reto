numero=20
def promedio_clima():
    valores = []
    for numero in range(1,20,1):
        try:
            valor = int(input("Temperatura: "))
            valores.append(valor)
        except ValueError:
            print("Inserta la temperatura:")
    print("Promedio: ", sum(valores)/20)

promedio_clima()