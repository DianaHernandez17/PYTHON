def imprimir_valores_ascendentes(diccionario):
    valores = sorted(diccionario.values()) 
    for valor in valores:
        print(valor)


mi_diccionario = {'a': 5, 'b': 2, 'c': 7, 'd': 1}
imprimir_valores_ascendentes(mi_diccionario)
