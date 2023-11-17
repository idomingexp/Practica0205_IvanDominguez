def contar_palabras(t):
    """Función que recoge un texto y nos cuenta cuantas veces está una palabra
    Parámetros:
        -t: texto donde contar las palabras
    Salida:
        Un diccionario con las palabras y su cuenta"""
    t = t.split()
    p = {}
    for x in t:
        if x in p:
            p[x] = p[x] + 1
        else:
            p[x] = 1
    return p

def palabra_mas_comun(p):
    """Función para ver la palabra más repetida del texto
    Parámetros:
        -p = Diccionario con las palabras y su cuenta
    Salida:
        La palabra más repetida con la veces que está"""
    mp = " "
    mv = 0
    for x, y in p.items():
        if y > mv:
            mp = x
            mv = y 
    return mp,mv

t = input("Introduce el texto a analizar:")
print("El diccionario es:", contar_palabras(t))
print("La palabra más repetida es:", palabra_mas_comun(contar_palabras(t)))
input()