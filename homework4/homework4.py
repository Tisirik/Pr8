def num_check(value):
        for i in range(len(value)):
                if value[i] in "0123456789,.-":
                    proove=1
                else:
                    proove=0
                    break
        return proove
print("Введените два числа")
num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
if num_check(num_1) == num_check(num_2)== 1:  
    num_1=float(num_1)
    num_2=float(num_2)
    if 0<num_1%1<5:
          num_1+=1
    if 0<num_2%1<5:
          num_2+=1
    a = num_1//1
    b = num_2//1
    if num_2 < num_1:
          b = num_1//1
          a = num_2//1
    for i in range(int(a),int(b)+1):
            print (i)
else:
       print('Вы ввели не число')
