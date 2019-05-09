def trapezoidal(f, x, y, xf, n):
    h = (xf-x)/float(n)
    xs = [0]
    ys = [1]
    while x < xf:
        x1 = x + h
        y1 = y + h * f(x, y);
        y1 = y + 0.5*h*(f(x,y)+f(x1,y1))
        xs.append(x1)
        ys.append(y1)
        x = x1
        y = y1
    return xs, ys