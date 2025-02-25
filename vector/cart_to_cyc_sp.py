import math

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)  # Radial distance
    theta = math.atan2(y, x)    # Azimuthal angle (radians)
    return r, theta, z

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)  # Radial distance
    theta = math.atan2(y, x)           # Azimuthal angle (radians)
    phi = math.acos(z / r) if r != 0 else 0  # Polar angle (radians)
    return r, theta, phi

# Example usage
x, y, z = 3, 4, 5
cylindrical = cartesian_to_cylindrical(x, y, z)
spherical = cartesian_to_spherical(x, y, z)

print("Cylindrical Coordinates (r, theta, z):", cylindrical)
print("Spherical Coordinates (r, theta, phi):", spherical)
