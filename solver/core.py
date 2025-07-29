import numpy as np
from .utils import compute_dt, compute_flux, compute_lambda

def shallow_water_solver(nx=100, L=10, C=0.8, g=1.0, nt=100, h_left=3, h_right=1):
    x = np.linspace(-L / 2, L / 2, nx)
    dx = x[1] - x[0]
    h_nx = np.ones(nx) * h_right
    h_nx[:nx // 2] = h_left
    hu_nx = np.zeros(nx)
    U = np.vstack((h_nx, hu_nx))
    U_record = np.zeros((2, nx, nt + 1))
    U_record[:, :, 0] = U
    dt_list = []
    t_record = np.zeros(nt + 1)

    for j in range(nt):
        dt = compute_dt(C, dx, U, g)
        dt_list.append(dt)
        U_new = np.zeros_like(U)
        for i in range(1, nx - 1):
            lam = compute_lambda(U[:, i], U[:, i + 1], g)
            F_r = 0.5 * (compute_flux(U[:, i], g) + compute_flux(U[:, i + 1], g)) - 0.5 * lam * (U[:, i + 1] - U[:, i])
            F_l = 0.5 * (compute_flux(U[:, i - 1], g) + compute_flux(U[:, i], g)) - 0.5 * lam * (U[:, i] - U[:, i - 1])
            U_new[:, i] = U[:, i] - dt / dx * (F_r - F_l)

        U_new[:, 0] = U_new[:, 1]
        U_new[:, -1] = U_new[:, -2]
        U = U_new
        U_record[:, :, j + 1] = U
        t_record[j + 1] = t_record[j] + dt

    return x, t_record, U_record
