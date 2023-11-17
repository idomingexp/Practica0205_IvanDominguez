def media(n):
    """Función que calcula la media de una serie de números
    Parámetros:
        -Lista de Números
    Salida:
        Media de todos los números introducidos"""
    m = 0
    n = n.split()
    for x in n:
        m = m + int(x)
    m = m / len(n)
    return("La media es: {}".format(m))

n = input("Dime una serie de números separados por espacios:")
print(media(n))
input()