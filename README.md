# Shallow Water Equation Solver (1D)

## Equations

This project solves the one-dimensional nonlinear shallow water equations:

\[
\frac{\partial h}{\partial t} + \frac{\partial (hu)}{\partial x} = 0
\]

\[
\frac{\partial (hu)}{\partial t} + \frac{\partial}{\partial x} \left( hu^2 + \frac{1}{2} g h^2 \right) = 0
\]

where:
- \( h(x,t) \): water height  
- \( u(x,t) \): velocity  
- \( g \): gravitational acceleration  

The equations are discretized using a finite volume method with Rusanov flux and explicit time stepping.

## Project Structure

- `main.py`: Main script to run the simulation and generate plots.
- `solver/`
  - `core.py`: Implements the shallow water solver.
  - `utils.py`: Computes fluxes, time steps, and wave speeds.
  - `plot.py`: Contains plotting functions for height and velocity.
- `README.md`: Project documentation.

## Usage

Run the main simulation:

```bash
python main.py
```

Modify simulation parameters such as domain length, number of grid points, CFL number, and initial conditions directly in `main.py`. The solver produces time snapshots of water height and velocity, plotted using matplotlib. 

## Notes

- No-flux boundary conditions are applied.
- Time step size is determined dynamically using the CFL condition.
- The code is organized to allow easy extension or reuse in other simulations.
