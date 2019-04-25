import copy
def SOR(A, b, x0, tol, w): 
    max_iter = 10000
    n = b.shape[0]
    x = x0.copy() 
    
    iters = 0
    while iters < max_iter: 
        iters += 1
        for i in range(n): 
            kp1_sum = np.dot(A[i, :i], x[:i])     #(20)
            k_sum = np.dot(A[i, i+1:], x0[i+1:])
            x[i] = (b[i] - (kp1_sum + k_sum)) / A[i, i]               # (22a)
            x[i] = np.dot(x[i], w) + np.dot(x0[i], (1 - w))         # (23)

        if (np.linalg.norm(x - x0) < tol): break 

        x0[:] = x

    return iters