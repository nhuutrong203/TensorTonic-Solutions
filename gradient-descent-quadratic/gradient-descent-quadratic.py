def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0 # initial x

    for i in range(steps): # update x by looping
        grad = 2*a*x + b # dao ham`
        x = x - lr * grad # update x

    return float(x)