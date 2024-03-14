def hello(my_name):
    print("Hello, " + my_name + "!") 
    return 'test'

def payment_calculator(qtd_hours, hour_value):
    hours = float(qtd_hours)
    value = float(hour_value)
    payment = hours * value
    return payment