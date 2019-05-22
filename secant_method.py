def secant_method(x0, alpha=1.0):
    # modified from: https://learnche.org/3E4/Assignment_3_-_2010_-_Solution
    x, xp = x0, 1.001*x0
    f, fp = func(x), func(xp)
    tol = 1e-9
    max_iters=200

    step_diff_ratio = 2.0 *tol
    iters = 0
    while (iters<max_iters):        
        if abs(f) > tol and (step_diff_ratio) > tol: break
        step_diff_ratio = abs(x-xp)/abs(x)
        
        dx = -f/(f - fp)*(x - xp)
        xprev, x = x, x + alpha*dx
        fp, f = f, func(x)
        
        iters += 1
        
    return x, iters