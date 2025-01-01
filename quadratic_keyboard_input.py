import math

# Get coefficients from the user
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

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
except ValueError:
    print("Invalid input. Please enter numeric values.")
