def task2():
    choice = int(input("""
1 -> your input list
2 -> generate list
"""))
    match choice:
        case 1: task2_input()
        case 2: task2_generate()
        case _:print("Wrong input")
   
def generate(n):
        for x in range(n):
            yield x

def task2_generate():
    
    sum = 0
    max_value = int(0)
    new_list = generate(10)
    
    for x in new_list:
        sum +=x
        if max_value < x:
            max_value = x
    
    print(f"Sum = {sum}         Max value is {max_value}")

def task2_input():
    
    sum = 0
    max_value = int(0)
    while True:
        number = int(input("write number(end = 0): "))
        if number == 0:
            break
        sum += number
        if max_value < number:
            max_value = number
        
    print(f"Sum = {sum}         Max value is {max_value}")