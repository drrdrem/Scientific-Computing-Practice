def newton(x, d):
    iters = 0
    f = np.array([[1],[1]])
    while True:
        if f.all() ==0 or iters == 10000: break
        # f
        f = np.array(
            [[-0.5*5281+5280/x[1][0]*np.sin(x[1][0])],
             [-5280/x[1][0]+x[0][0]+5280/x[1][0]*np.cos(x[1][0])]])

        # Df
        Df = np.array(
            [[0, -5280/(x[1][0]**2)*np.sin(x[1][0])+5280/x[1][0]*np.cos(x[1][0])],
             [1, -5280/(x[1][0]**2)*(np.cos(x[1][0])+1)-5280/x[1][0]*np.sin(x[1][0])]])

        # Updating x
        x = x - np.linalg.pinv(Df).dot(f)
        x = np.array([[np.round(x[0][0],d)], [np.round(x[1][0],d)]])

        # Evaluating new f
        f = np.array([[-0.5*5281+5280/x[1][0]*np.sin(x[1][0])],
                  [-5280/x[1][0]+x[0][0]+5280/x[1][0]*np.cos(x[1][0])]])
        f = np.array([[np.round(f[0][0],d)], [np.round(f[1][0],d)]])
        
        iters += 1
    return x, f, iters