def saludo(n):
    """Función que saluda
    Parámetros:
        -n: Nombre de la persona a saludar
    Salida:
        Saludo con el nombre de la persona"""

    return("¡Hola {}!".format(n))

n = input("Dime tu nombre:")
print(saludo(n))
input()