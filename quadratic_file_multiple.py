import math

# Read coefficients from a file
try:
    with open("input1.txt", "r") as file:
        lines = file.readlines()

    results = []
    for line in lines:
        try:
            a, b, c = map(float, line.strip().split())
            if a == 0:
                results.append("Not a quadratic equation (a cannot be 0).")
            else:
                discriminant = b**2 - 4*a*c
                if discriminant < 0:
                    results.append("No real roots exist.")
                else:
                    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                    results.append(f"Roots are: {root1} and {root2}")
        except ValueError:
            results.append("Invalid input format.")

    # Write results to an output file
    with open("output.txt", "w") as output_file:
        for result in results:
            output_file.write(result + "\n")

    print("Results have been written to 'output.txt'.")
except FileNotFoundError:
    print("File not found. Please ensure 'input1.txt' exists.")
