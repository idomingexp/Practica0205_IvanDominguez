def area_circulo(r):
    """Función que calcula el área de un círculo
    Parámetros:
        -r: radio del círculo
    Salida:
        Área del círculo"""
    import math
    return (math.pi * r ** 2)

def volumen_cilindro(h):
    """Función que calcula el volumen de un cilindro
    Parámetros:
        -h: altura del cilindro
    Salida:
        Volumen del cilindro"""
    return (area_circulo(r) * h)

r = float(input("Dime el radio:"))
h = float(input("Dime la altura:"))
print("El área del círculo es: {}. Y el volumen del cilindro es: {}".format(area_circulo(r), volumen_cilindro(h)))
input()    