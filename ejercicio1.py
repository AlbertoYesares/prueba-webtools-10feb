# Ejercicio 1. Prueba ténica WebTools Alberto Yesares
# Escribe una función en Python que reciba una lista de números y devuelva otra lista con los números duplicados eliminados, manteniendo el orden original.

def elimina_duplicados(lista):
    lista_unicos = []
    conjunto_unico = set()
    for numero in lista:
        if numero not in conjunto_unico:
            conjunto_unico.add(numero)
            lista_unicos.append(numero)
    return lista_unicos

"""
Por un tema de rendimiento, es algo mejor utilizar un conjunto (conjunto_unico), 
ya que haría la verificación más rápido que si NO existiera el conjunto y solo comparara
con la lista_unicos, por ejemplo así:

def elimina_duplicados(lista):
    lista_unicos = []
    for numero in lista:
        if numero not in lista_unicos:
            lista_unicos.append(numero)
    return lista_unicos

Aunque el código sería más corto, pero para listas largas de números no sería tan eficiente
"""

lista_duplicados = [3, 5, 2, 3, 8, 5, 2, 10]
lista_sin_duplicados = elimina_duplicados(lista_duplicados)
print(lista_sin_duplicados)