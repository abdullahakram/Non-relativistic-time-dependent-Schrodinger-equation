import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

# Define the problem parameters
L = 10    # Box length
N = 200   # Number of grid points
x = np.linspace(0, L, N, endpoint=False)    # Grid points
dx = x[1] - x[0]   # Grid spacing
V = 0.5 * x**2   # Potential energy function
m = 1    # Particle mass
hbar = 1   # Planck's constant

# Construct the Hamiltonian matrix
diagonal = np.ones(N) / dx**2 + V
off_diagonal = -0.5 * np.ones(N-1) / dx**2
H = sp.diags([off_diagonal, diagonal, off_diagonal], [-1, 0, 1], format='csr')
H /= -2 * m * hbar

# Define the initial wavefunction
sigma = 0.5
k = 10
psi0 = np.exp(-(x-L/2)**2/(2*sigma**2)) * np.exp(1j*k*x)

# Set the time step and number of time steps
dt = 0.01
timesteps = 200

# Solve the time-dependent Schrödinger equation
psi = psi0
for i in range(timesteps):
    psi = spla.expm_multiply(-1j*H*dt, psi)

# Plot the final wavefunction
plt.plot(x, np.abs(psi)**2)
plt.xlabel('x')
plt.ylabel('|psi(x)|^2')
plt.show()
