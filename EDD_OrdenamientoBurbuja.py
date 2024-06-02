def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Solicitar al usuario que ingrese una lista de números
lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

lista_ordenada = ordenamiento_burbuja(lista)
print("Lista ordenada:", lista_ordenada)
