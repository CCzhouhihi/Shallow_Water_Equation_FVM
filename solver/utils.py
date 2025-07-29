import numpy as np

def compute_dt(C, dx, U, g):
    h = U[0, :]
    u = U[1, :] / h
    lambda1 = u + np.sqrt(g * h)
    lambda2 = u - np.sqrt(g * h)
    max_lambda = np.max(np.abs(np.concatenate((lambda1, lambda2))))
    return C * dx / max_lambda

def compute_flux(Uj, g):
    h = Uj[0]
    hu = Uj[1]
    u = hu / h
    Fh = hu
    Fhu = hu * u + g * h**2 / 2
    return np.array([Fh, Fhu])

def compute_lambda(Uj, Uj1, g):
    h_j, hu_j = Uj
    h_j1, hu_j1 = Uj1
    u_j = hu_j / h_j
    u_j1 = hu_j1 / h_j1
    lambdas = [
        u_j + np.sqrt(g * h_j),
        u_j1 + np.sqrt(g * h_j1),
        u_j - np.sqrt(g * h_j),
        u_j1 - np.sqrt(g * h_j1)
    ]
    return np.max(np.abs(lambdas))
