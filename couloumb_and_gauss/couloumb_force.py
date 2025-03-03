import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

def s_function(t):
    e_0 = 8.854e-12
    r_1 = np.array([7, -8, -10])
    r_2 = np.array([4, -5, 6])
    r_3 = np.array([1, 2, -3])
    m = 5
    q_1 = -5e-6
    q_2 = 4e-6
    q_3 = -5e-6

    k = 1 / (4 * math.pi * e_0)

    F_12 = ((q_1 * q_2 * k) / np.linalg.norm(r_1 - r_2)) * ((r_1 - r_2) / np.linalg.norm(r_1 - r_2))
    F_13 = ((q_1 * q_3 * k) / np.linalg.norm(r_1 - r_3)) * ((r_1 - r_3) / np.linalg.norm(r_1 - r_3))
    F_23 = ((q_2 * q_3 * k) / np.linalg.norm(r_2 - r_3)) * ((r_2 - r_3) / np.linalg.norm(r_2 - r_3))

    F_q1 = F_12 + F_13
    F_q2 = F_23 - F_13
    F_q3 = -(F_23 + F_12)

    a1 = F_q1 / m
    a2 = F_q2 / m
    a3 = F_q3 / m

    s1 = 0.5 * a1 * t**2
    s2 = 0.5 * a2 * t**2
    s3 = 0.5 * a3 * t**2

    return r_1 + s1, r_2 + s2, r_3 + s3

# Setup figure dan axes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_zlim(-15, 15)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mendapatkan posisi awal (t=0)
init_pos = s_function(0)
x_init = [init_pos[0][0], init_pos[1][0], init_pos[2][0]]
y_init = [init_pos[0][1], init_pos[1][1], init_pos[2][1]]
z_init = [init_pos[0][2], init_pos[1][2], init_pos[2][2]]

# Warna berbeda untuk tiap muatan
colors = ['red', 'green', 'blue'] #red :q1, green :q2, blue:q3

# Inisialisasi scatter plot dengan posisi awal
scatter = ax.scatter(x_init, y_init, z_init, c=colors, s=100)

def init():
    # Set posisi awal pada scatter plot 3D
    scatter._offsets3d = (x_init, y_init, z_init)
    return scatter,

def update(frame):
    t = frame * 0.1  # Menambahkan waktu dalam animasi
    s1, s2, s3 = s_function(t)
    
    x_data = [s1[0], s2[0], s3[0]]
    y_data = [s1[1], s2[1], s3[1]]
    z_data = [s1[2], s2[2], s3[2]]
    
    scatter._offsets3d = (x_data, y_data, z_data)
    scatter.set_color(colors)
    return scatter,

ani = FuncAnimation(fig, update, frames=5000, init_func=init, interval=50, blit=False)
plt.show()
