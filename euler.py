def euler(f, x0, y0, xf, n):
    h = (xf-x0)/float(n)
    x = np.linspace(x0, xf, n+1)
    y  =  np.zeros([n+1])
    y[0] = y0
    for i in range(1, n+1):
        y[i] = h*(f(x[i-1], y[i-1])) + y[i-1]
    return x, y