first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
# elif first == third and first != second:
#     print(2)
# elif first == third and second != third or first == second and first != third or first != third and second == third:
#     print(2)
# #elif first != second and  second != third:
#   # print(0)

# if first == second and second == third:
#     print(3)
# elif first != second and second != third and first == third:
#     print(2)
# else:
#     print(0)