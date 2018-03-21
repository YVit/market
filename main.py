x = 10
print(x)
array = [1, 89, 9, "Привет"]
print( len(array) )
full_names = [['Миша', 'Иванов'], ['Саша', 'Петров']]
print( full_names[1][0] )
person = {'name': 'Vit', 'age': 30, 'job': 'programmer'}
print( person['name'] )
person_list = {'first': {'age': 30 }, 'second': {'score': 56}}
print( person_list['first']['age'])

def print_name():
        name = ['Vit']
        age = 29
        if age > 30:
            print('Возраст больше 30')
        elif age < 30:
            print('Возраст меньше 30')
        for n in name:
            print('Здраствуйте, ' + n)
print_name()
