import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 0.1  # reaction rate constant (arbitrary units)
A0 = 1.0  # initial concentration of acetyl (M)
H2O0 = 1.0  # initial concentration of water (M)
P0 = 0.0  # initial concentration of product (M)

# Time settings
t = np.linspace(0, 100, 100)  # time from 0 to 100 seconds

# Concentration calculations using first-order kinetics
A_concentration = A0 * np.exp(-k * t)  # Concentration of acetyl
H2O_concentration = H2O0  # Concentration of water remains constant
P_concentration = P0 + (A0 - A_concentration)  # Concentration of product

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t, A_concentration, label='Acetyl (A)', color='blue')
plt.plot(t, H2O_concentration * np.ones_like(t), label='Water (H2O)', color='green', linestyle='--')
plt.plot(t, P_concentration, label='Product (P)', color='red')

# Adding labels and title
plt.title('Acetyl Hydrolysis Reaction')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (M)')
plt.legend()
plt.grid()
plt.ylim(0, 1.1)
plt.xlim(0, 100)
plt.show()
