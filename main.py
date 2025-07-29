from solver.core import shallow_water_solver
from solver.plot import plot_shallow_water

x, t_record, U_record = shallow_water_solver(nx=100, L=10, C=0.8, g=1.0, nt=100, h_left=3, h_right=1)
plot_shallow_water(x, t_record, U_record)
