# Task 7: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("Contents of the file:")
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
