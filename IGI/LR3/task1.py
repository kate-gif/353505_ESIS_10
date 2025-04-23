def task1():
    i = 0
    x = float(input("write |x|<1: "))
    eps = int(input("write accuracy: "))
    iteration = int (input("number of iteration (i <= 500): "))
    result = 0

    if iteration > 500 or iteration < 0:
        print("wrong number of iteration")
        return 
    
    if abs(x)<1:
        while i<=iteration:
            result += pow(x, i)
            i+=1
        result = str(result)    
        print(f"x = {x}       n = {iteration}       F(x) = {result[:eps+2]}         Math F(x) = {1/(1-x)}       eps = {eps}")
        
    else:
        print("wrong number")
   

