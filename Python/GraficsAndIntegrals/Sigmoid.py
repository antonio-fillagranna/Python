import matplotlib.pyplot as plt
import numpy as np
from scipy.special import expit


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


print(sigmoid(0.5))  # Return: 0.6224593312018546

sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

sigmoid_val = expit(2)  # Calculate sigmoid value for x=2
print(sigmoid_val)  # Approximately 0.88079
# Create a range of x values
x_values = np.linspace(-10, 10, 1000)

# Calculate corresponding y values using the sigmoid formula
y_values = sigmoid(x_values)

# Plot the sigmoid function
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Sigmoid Function", color="b")
plt.title("The Sigmoid Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
