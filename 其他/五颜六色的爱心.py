import numpy as np
import matplotlib.pyplot as plt

# Heart shape function
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Create a figure and axis
fig, ax = plt.subplots()

# Generate values for t
t = np.linspace(0, 2 * np.pi, 1000)

# Generate heart shape coordinates
x, y = heart_shape(t)

# Create a scatter plot with gradient colors
colors = plt.cm.rainbow(np.linspace(0, 1, len(t)))
for i in range(len(t) - 1):
    ax.plot(x[i:i+2], y[i:i+2], color=colors[i], linewidth=2)

# Remove the axes
ax.axis('off')

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Show the plot
plt.show()
