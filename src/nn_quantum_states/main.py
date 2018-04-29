from nn_quantum_states.networks.rbm import RBM
from nn_quantum_states.hamiltonians.ising1d import Ising1D
import matplotlib.pyplot as plt
from nn_quantum_states.data.generator import Generator
import numpy as np

import sys
sys.path.insert(0, './')

num_spins = 4
alpha = 2


iterations = 7500
epochs = 75
hami = Ising1D('Ising Model', num_spins, h=2)
model = RBM(num_spins, alpha * num_spins, hami, lr=1)
Energies = model.optimize(epochs, iterations)

plt.figure()
plt.plot(range(epochs), Energies)
plt.xlabel('Iteration')
plt.ylabel('$E_{loc}$')
plt.title('Energy vs. Iteration')
plt.show()
