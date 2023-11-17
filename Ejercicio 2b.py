def factorial(n):
    """Función que calcula el factorial de un entero
    Parámetros:
        -n: Nº del que hacer factorial
    Salida:
        El número ya factorizado"""
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

n = int(input("Dime un Nº entero:"))
print(factorial(n))
input()