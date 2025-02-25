import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Convert to NumPy arrays
v_1 = np.array([2, 2, 3])
v_2 = np.array([2, 11, 5])

# Vector operations
cross_product = np.cross(v_1,v_2)       # cross_product
dot_product=np.dot(v_1,v_2)

print(f"dot_product = {dot_product}")

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin for vectors
origin = np.array([0, 0, 0])

# Vectors to plot
vectors = [v_1, v_2, cross_product]
colors = ['r', 'g', 'b']  # Different colors for clarity
labels = ['v1', 'v2', 'cross_product']

# Define arrow scaling
arrow_length = 1  # Ensures all arrowheads are uniform

# Plot vectors with fixed arrowhead sizes
for vec, color, label in zip(vectors, colors, labels):
    ax.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.1)  # Adjust arrow_length_ratio for uniformity

# Set limits for better visualization
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Labels and grid
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D Vector Operations Visualization")
ax.legend()
ax.grid()

# Show the plot
plt.show()
