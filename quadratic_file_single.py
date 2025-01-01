import math

# Read coefficients from a file
try:
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        a, b, c = map(float, line.split())

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
except FileNotFoundError:
    print("File not found. Please ensure 'input.txt' exists.")
except ValueError:
    print("Invalid file format. Ensure the file contains three numeric values.")
