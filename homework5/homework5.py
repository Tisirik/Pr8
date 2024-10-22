input_num=0
Trigger=True
while Trigger:
    print("Введите число")
    number=input()
    if number=="end" or number=='stop':
        Trigger=False
        break
    else:
        for i in range(len(number)):
            if number[i] in "0123456789,.-":
                proove=1
            else:
                proove=0
                break
        if proove==1:
            input_num+=float(number)
        else:
            print("введите число, а не буквы")
            Trigger=False
            break
print(input_num)