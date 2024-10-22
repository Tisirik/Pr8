print('Введите два целых числа')
while True:
    num_1 = input("Введите первое число: ")
    num_2 = input("Введите второе число: ")

    if num_1.lstrip('-').isdigit() and num_2.lstrip('-').isdigit():
        print("Сумма:", int(num_1) + int(num_2))
    else:
        print("Введите целые числа!")