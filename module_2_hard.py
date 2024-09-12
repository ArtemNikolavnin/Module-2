import random
def field():
    field_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(field_1)
    return n
n = field()
def freedom(number):
    freedom = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                freedom += str(i) + str(j)
    return freedom
    
result = freedom(n)
print('Цифра:', n)
print('Пароль:', result)
