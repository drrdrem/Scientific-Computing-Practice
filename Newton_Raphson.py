from sympy import diff
from math import tan

def Newton_Raphson(func, a):
    '''
    func: str of function eg: "tan(x)"

    modified from: https://www.itread01.com/content/1544862813.html 
    '''
    maxit = 200
    iters = 0
    while iters<maxit:
        x = a
        c = a - ( eval(func)) / eval(str(diff(func)))
        x = c
        a = c
        iters+=1
        if  abs(eval(func)) < 1e-9:
            return  c, iters