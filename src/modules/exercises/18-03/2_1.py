def calcular_bolos(A, B, C):
    bolos_farinha = A // 2
    bolos_ovos = B // 3
    bolos_leite = C // 5

    return min(bolos_farinha, bolos_ovos, bolos_leite)

A, B, C = map(int, input().split())

print(calcular_bolos(A, B, C))
