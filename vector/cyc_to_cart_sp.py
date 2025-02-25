import math

def cylindrical_to_cartesian(r, theta, z):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y, z

def cylindrical_to_spherical(r, theta, z):
    x, y, z = cylindrical_to_cartesian(r, theta, z)
    return cartesian_to_spherical(x, y, z)

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)  # Radial distance
    theta = math.atan2(y, x)           # Azimuthal angle (radians)
    phi = math.acos(z / r) if r != 0 else 0  # Polar angle (radians)
    return r, theta, phi

# Example usage
r, theta, z = 5, math.radians(45), 3
cartesian = cylindrical_to_cartesian(r, theta, z)
spherical = cylindrical_to_spherical(r, theta, z)

print("Cartesian Coordinates (x, y, z):", cartesian)
print("Spherical Coordinates (r, theta, phi):", spherical)
