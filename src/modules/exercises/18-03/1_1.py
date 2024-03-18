peopleQuantity = int(input('Enter the number of people: '))
valueBill = float(input('Enter the value of the bill: '))
tip = valueBill * 0.1
valuePerPerson = (valueBill + tip) / peopleQuantity

print(tip, valuePerPerson)