from random import randint

def somaPares (tupla):
  soma = 0
  for i in tupla:
    if i % 2 == 0:
      soma += i
  return soma

print(somaPares((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # 30


def sum10RandomNumbers():
  sum = 0 
  for count in range(10)
    sum += randint(1, 5)
  return sum

print(sum10RandomNumbers()) # 543