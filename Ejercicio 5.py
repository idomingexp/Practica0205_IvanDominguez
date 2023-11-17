def cuadrado(n):
    """Función que recibe unos números y los devuelve al cuadrado
    Parámetros:
        -n: lista de los números
    Salida:
        Lista de los números al cuadrado"""
    c = []
    n = n.split()
    for x in range(len(n)):
        c.append(int(n[x]) ** 2)
    return c

n = input("Dime una lista de números separados por espacios:")
print(cuadrado(n))
input()
