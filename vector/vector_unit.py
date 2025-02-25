import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Convert to NumPy arrays
v_1 = np.array([2, 2, 3])
v_2 = np.array([2, 11, 5])

# Vector operations
unit_1 = v_1/(math.sqrt((v_1[0]**2)+(v_1[1]**2)+(v_1[2]**2)))       # vector_unit_1
unit_2 = v_2/(math.sqrt((v_2[0]**2)+(v_2[1]**2)+(v_2[2]**2)))        # vector_unit_2

print(f"unit_1 = {unit_1}\nunit_2 = {unit_2}")

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin for vectors
origin = np.array([0, 0, 0])

# Vectors to plot
vectors = [v_1, v_2, unit_1,unit_2]
colors = ['r', 'g', 'b','y']  # Different colors for clarity
labels = ['v1', 'v2', 'unit_1','unit_2']

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
