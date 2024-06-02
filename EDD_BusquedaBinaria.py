def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  

lista = list(map(int, input("Ingrese una lista de numeros ordenados separados por espacios: ").split()))

objetivo = int(input("Ingrese el numero que desea buscar: "))

resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f'El elemento {objetivo} se encuentra en el indice {resultado}.')
else:
    print(f'El elemento {objetivo} no se encuentra en la lista.')
