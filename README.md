# Non-relativistic time-dependent Schrödinger equation

The non-relativistic time-dependent Schrödinger equation is a fundamental equation in quantum mechanics that describes the time evolution of a quantum state. It is given by:

iħ ∂Ψ/∂t = HΨ

where ħ is the reduced Planck constant, Ψ is the wavefunction of a quantum system, and H is the Hamiltonian operator, which describes the total energy of the system. The equation states that the rate of change of the wavefunction with respect to time is proportional to the Hamiltonian acting on the wavefunction.

The wavefunction Ψ contains all the information about the quantum state of the system, including its position, momentum, and other physical properties. The absolute square of the wavefunction |Ψ|^2 gives the probability density of finding the system in a particular state.

The time-dependent Schrödinger equation is a partial differential equation, which means that it describes how the wavefunction varies with both time and position. In practice, the equation is often solved numerically using computational methods such as finite differences or spectral methods.

The non-relativistic version of the Schrödinger equation applies to systems in which the velocities of the particles are much smaller than the speed of light, so that relativistic effects can be neglected. It is a cornerstone of quantum mechanics and is used to study a wide range of physical systems, from atoms and molecules to condensed matter and quantum field theory.

In this code we first define the problem parameters such as the length of the box, number of grid points, potential energy function, particle mass, and Planck's constant. We then construct the Hamiltonian matrix using sparse matrix operations provided by the scipy.sparse module.

Next, we define the initial wavefunction as a Gaussian wavepacket centered at the middle of the box with a momentum of 10. We also set the time step and number of time steps for the simulation.

Finally, we solve the time-dependent Schrödinger equation using the matrix exponential method provided by the scipy.sparse.linalg.expm_multiply function. This function computes the matrix exponential of -iHdt, which represents the time evolution operator for a small time step dt. We apply this operator to the wavefunction at each time step to obtain the time-evolved wavefunction.

Finally, we plot the absolute square of the wavefunction at the end of the simulation to visualize the probability density of the particle in the box.
