import numpy as np
import matplotlib.pyplot as plt

def plot_shallow_water(x, t_record, U_record, t_list=[0, 0.5, 2]):
    h_record = U_record[0, :, :]
    u_record = U_record[1, :, :] / U_record[0, :, :]
    nt_list = [np.argmin(np.abs(t_record - t)) for t in t_list]

    fig, axs = plt.subplots(len(t_list), 2, figsize=(12, 3 * len(t_list)))
    for i, t_idx in enumerate(nt_list):
        axs[i, 0].plot(x, h_record[:, t_idx], linewidth=2)
        axs[i, 1].plot(x, u_record[:, t_idx], linewidth=2)
        axs[i, 0].set_ylabel('h'), axs[i, 1].set_ylabel('u')
        axs[i, 0].set_title(f't = {t_list[i]}'), axs[i, 1].set_title(f't = {t_list[i]}')
        axs[i, 0].grid(), axs[i, 1].grid()

    for ax in axs.flat:
        ax.set_xlabel('x')
    plt.tight_layout()
    plt.show()
