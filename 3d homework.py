# Создайте массив состоящий из 5ти словарей
school = [
    {'pen': 'blue'},
    {'pencil': 1},
    {'note': 15},
    {'book': 'geography'},
    {'ruler': 20},
]
print(school)

# Создайте массив состоящий из 5ти массивов с любыми значениями
arr_arr = [['river', 'ocean'], [100, 200, 300], ['cat', 'dog'], ['phone', 'tv', 'laptop'], ['blue', 'black', 'red']]
print(arr_arr)


# Замените в ранее созданном массиве несколько значений
school[0]['pen'] = 'red'
print(school[0]['pen'])

school[0]['note'] = 9
print(school[0]['note'])


# Создайте цикл для первого масссива
for first in school:
    print(first)


# Создайте цикл для второго масссива
for second in arr_arr:
    if second == arr_arr[3]:
        print('numbers')

# Создайте массив состоящий из 10 цифр от 0 и до 20
arr3 = [0, 1, 5, 10, 15, 16, 18, 20, 8, 9]
print(arr3)
# Пройдитесь циклом по вышесозданному массиву и выведите все числа которые больше 10ти
for great in arr3:
    if great >= 10:
        print(great)

# Создайте словарь который содержит в себе все типы данных которые мы проходили (ключи на ваше усмотрение)
# --- > Здесь опишите решение
dictionary = {
    'name': 'symbat',
    'age': 19,
    'hobby': ['programming', 'read', 'music'],
    'earth': {'sun', 'sky'
    }
}
print(dictionary)

# Создайте словарь который содержит в себе 5 разных массивов
s = {
    'first': [12, 33, 78, 99],
    'second': [14, 66, 89, 0],
    'third': [100, 105, 221],
    'fourth': ['dinosuar', 'animal'],
    'fifth': ['english', 'russian'],
}
print(s)

# Создайте условия if / else
num = 1
if num > 10:
    print(num, 'is greater than 10')
else:
    print(num, 'is less than 10')


# Создайте условия if / elif / else
a = 'morning'
if a == 'morning':
    print('good morning')
elif a == "afternoon":
    print('good afternoon')
else:
    print('good night' )

# Создайте условия if / elif / elif / else
country = 'USA'
if country == 'USA':
    print('Washington')
elif country == 'Kyrgyzstan':
    print('Bishkek')
elif country == 'Thailand':
    print('Bangkok')
else:
    print('nothing')


# Создайте условия цикл который проходится по массиву в который содержит в себе условия if / elif / else
# --- > Здесь опишите решение
number = 0

if number > 0:
    print('number is > 0')
elif number == 0:
    print('number is = 0')
else:
    print('number < 0')
