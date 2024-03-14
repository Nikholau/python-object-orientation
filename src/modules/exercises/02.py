value = float(input('Enter the value: '))
sugarplumPrice = float(input('Enter the price of the sugarplum: '))

if sugarplumPrice > value:
  print('The value is not enough to buy a sugarplum')
  exit()

quantity = value // sugarplumPrice
print(quantity)

change = value % sugarplumPrice
print(change)