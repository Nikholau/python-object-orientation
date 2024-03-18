def ordenar_lista(n, lista):
    lista.sort()
    return lista

n = int(input())

lista = list(map(int, input().split()))

print(*ordenar_lista(n, lista))
