def task5():
    numbers = []
    min_value = float('inf')
    sum = 0
    i = 0
    L = -1
    I = 0
        
    while True:
        try:
            number = float(input("write number: "))
            numbers.append(number)
            
            
            if number > 0:
                if L == -1:
                    L=i
                else:
                    I = i
                if number < min_value:
                    min_value = number
            i += 1
        except ValueError:
            print("stop input")
            break

    print( f"test{numbers[L:I+1]}")

    for element in numbers[L:I+1]:
        sum +=element 

    if numbers:  
        print(f"Минимальное положительное значение: {min_value}")
        print(f"Сумма чисел: {sum}")
        print(f"Все введенные числа: {numbers}")
    else:
        print("Не было введено ни одного числа")

def task5():
    numbers = []
    min_value = float('inf')
    sum = 0
    i = 0
    L = -1
    I = 0
        
    while True:
        try:
            number = float(input("write number: "))
            numbers.append(number)
            
            
            if number > 0:
                if L == -1:
                    L=i
                else:
                    I = i
                if number < min_value:
                    min_value = number
            i += 1
        except ValueError:
            print("stop input")
            break

    print( f"test{numbers[L:I+1]}")

    for element in numbers[L:I+1]:
        sum +=element 

    if numbers:  
        print(f"Минимальное положительное значение: {min_value}")
        print(f"Сумма чисел: {sum}")
        print(f"Все введенные числа: {numbers}")
    else:
        print("Не было введено ни одного числа")