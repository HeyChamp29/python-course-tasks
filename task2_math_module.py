import math

# Ask the user for input
num = float(input("Enter a number: "))

# Perform calculations using the math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display results
print(f"\nSquare root of {num} is: {sqrt_val}")
print(f"Natural logarithm of {num} is: {log_val}")
print(f"Sine of {num} (in radians) is: {sine_val}")
