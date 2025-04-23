#Esis Ekaterina  353505 lr3 var - 10

#TO DO: генератор, декоратор


import task1
import task2 
import task3
import task4
import task5

def main():
    while True:
        try:
            menu = int(input("Choose task (1-5, any other to exit): "))
            match menu:
                case 1: task1.task1()
                case 2: task2.task2()
                case 3: task3.task3()
                case 4: task4.task4()
                case 5: task5.task5()
                case _: 
                    print("End of work")
                    break
        except ValueError:
            print("Please enter a number")
            continue
    
    decorated_task3 = task3.decoration(task3.task3)

    result = decorated_task3()
    if result:
        print("Результат:", result)
    
if __name__ == "__main__":
    main()










