import math

# Hard-coded coefficients
a = 1
b = -3
c = 2

# Solve the quadratic equation
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No real roots exist.")
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots are: {root1} and {root2}")
