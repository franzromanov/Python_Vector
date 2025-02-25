import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


#calculation
x_sym, y_sym = sp.symbols('x y')
P_sym = x_sym-y_sym
Q_sym = y_sym+x_sym

div_sym = sp.diff(P_sym, x_sym) + sp.diff(Q_sym, y_sym)
curl_sym = sp.diff(Q_sym, x_sym) - sp.diff(P_sym, y_sym)

div_func = sp.lambdify((x_sym, y_sym), div_sym, 'numpy')
curl_func = sp.lambdify((x_sym, y_sym), curl_sym, 'numpy')


#defining vector field
def P(x, y):
    return x-y

def Q(x, y):
    return y+x

fig, (ax_field, ax_info) = plt.subplots(1, 2, figsize=(12, 6))

x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
U = P(X, Y)
V = Q(X, Y)
ax_field.quiver(X, Y, U, V, color='b')
ax_field.set_title('Vector Field F(x, y) = (x, y)')
ax_field.set_xlabel('x')
ax_field.set_ylabel('y')
ax_field.axhline(0, color='black', linewidth=0.5)
ax_field.axvline(0, color='black', linewidth=0.5)
ax_field.grid(color='gray', linestyle='--', linewidth=0.5)

theta = np.linspace(0, 2 * np.pi, 100)
path_x = 3 * np.cos(theta)
path_y = 3 * np.sin(theta)
ax_field.plot(path_x, path_y, 'r', label='Path')
ax_field.legend()

ax_info.axis('off')
info_text = ax_info.text(0.05, 0.5, "Click on the vector field\nfor divergence and curl info.", fontsize=14, va='center', ha='left')

def onclick(event):
    if event.inaxes == ax_field:
        x_click = event.xdata
        y_click = event.ydata
        div_val = div_func(x_click, y_click)
        curl_val = curl_func(x_click, y_click)
        text = (f"At (x, y) = ({x_click:.2f}, {y_click:.2f}):\n\n"
                f"Divergence = {div_val:.2f}\n"
                f"Curl       = {curl_val:.2f}")
        info_text.set_text(text)
        fig.canvas.draw_idle()

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.tight_layout()
plt.show()
