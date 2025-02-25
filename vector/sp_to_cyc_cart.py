import math

def spherical_to_cartesian(r, theta, phi):
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

def spherical_to_cylindrical(r, theta, phi):
    x, y, z = spherical_to_cartesian(r, theta, phi)
    return cartesian_to_cylindrical(x, y, z)

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)  # Radial distance
    theta = math.atan2(y, x)    # Azimuthal angle (radians)
    return r, theta, z

# Example usage
r, theta, phi = 5, math.radians(45), math.radians(30)
cartesian = spherical_to_cartesian(r, theta, phi)
cylindrical = spherical_to_cylindrical(r, theta, phi)

print("Cartesian Coordinates (x, y, z):", cartesian)
print("Cylindrical Coordinates (r, theta, z):", cylindrical)
