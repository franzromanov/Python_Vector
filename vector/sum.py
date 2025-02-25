import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Convert to NumPy arrays
v_1 = np.array([1, 2, 3])
v_2 = np.array([2, 2, 4])

# Vector operations
sum_ = v_1 + v_2       # Vector addition
sub_ = v_1 - v_2       # Vector subtraction
div_const = v_1 / 2    # Division by constant
mul_const = v_1 * 2    # Multiplication by constant

# Print results
print(f"\033[0;37msum:{sum_}\nsubtraction:{sub_}\ndivision_with_constant:{div_const}\nmultiplication_with_constant:{mul_const}")

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Origin for vectors
origin = np.array([0, 0, 0])

# Vectors to plot
vectors = [v_1, v_2, sum_, sub_, div_const, mul_const]
colors = ['r', 'g', 'b', 'y', 'm', 'c']  # Different colors for clarity
labels = ['v1', 'v2', 'sum', 'sub', 'div_const', 'mul_const']

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
