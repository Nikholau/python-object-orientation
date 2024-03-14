lang = input('What is your favorite programming language? ')

match lang:
    case 'Python':
        print('You chose Python.')
    case 'C':
        print('You chose C.')
    case 'Java':
        print('You chose Java.')
    case _:
        print('You chose something else.')