import matplotlib.pyplot as plt
import numpy as np
import math

# Define the range of input sizes
n = np.linspace(1, 20, 400)

# Define the functions
log_n = np.log(n)
n = n
two_n = 2 * n
sqrt_n = np.sqrt(n)
n_log_n = n * np.log(n)
two_n_squared = 2 * n**2
n_cubed = n**3 + 3 * n**2
n_factorial = [math.factorial(int(i)) for i in n]

# Plot the functions
plt.figure(figsize=(10, 6))
plt.plot(n, log_n, label='log(n)')
plt.plot(n, n, label='n')
plt.plot(n, two_n, label='2n')
plt.plot(n, sqrt_n, label='sqrt(n)')
plt.plot(n, n_log_n, label='n log(n)')
plt.plot(n, two_n_squared, label='2n^2')
plt.plot(n, n_cubed, label='n^3 + 3n^2')
plt.plot(n, n_factorial, label='n!')

# Add labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.title('Time Complexity of Functions')
plt.legend()

# Use a logarithmic scale for the y-axis
plt.yscale('log')

# Show the plot
plt.show()
