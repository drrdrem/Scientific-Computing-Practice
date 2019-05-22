def false_position(func, a , b): 
    # modified from: https://www.geeksforgeeks.org/program-for-method-of-false-position/
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
    maxit = 200  
    c = a
    iters = 0
    while iters < maxit: 
        iters+=1

        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
        if abs(func(c)) == 0: 
            return c, iters
        elif func(c) * func(a) < 0: 
            b = c
        else: 
            a = c    

    return c, iters