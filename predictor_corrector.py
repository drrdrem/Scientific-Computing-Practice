import copy
def predictor_corrector(f, x0, y0, xf, n, correct_flag = 'Milnes'):
    h = (xf-x0)/float(n)
    x = np.linspace(x0, xf, n+1)
    y  =  np.zeros([n+1])
    for i in range(n+1):
        x , y = euler(f, x0, y0, xf, n)
   
    for i in range(4, n+1):
        y0 = y.copy()
        y0[i] = y0[i-4] + (4*h/3) * 
        (2*f(x[i-1], y0[i-1]) -f(x[i-2], y0[i-2])+2*f(x[i-3], y0[i-3]))
        yk = y0.copy()
        for _ in range(10):
            yk[i] = (9/8)*yk[i-1] -(1/8)*yk[i-3]+ (3*h/8) * 
            (f(x[i], yk[i]) + 2*f(x[i-1], yk[i-1]) -f(x[i-2], yk[i-2]))
        if correct_flag == 'None':
            y[i] = yk[i]
        if correct_flag == 'Milnes':
            y[i] = y0[i] + (28/29)*(yk[i]-y0[i])
        if correct_flag == 'Hamming':
            y[i] = y0[i] + (112/121)*(yk[i]-y0[i])
            
    return x, y