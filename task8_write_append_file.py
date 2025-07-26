# Task 8: Write and Append Data to a File

# Write to file
text1 = input("Enter some text to write into the file: ")
with open("output.txt", "w") as file:
    file.write(text1 + "\n")

# Append to file
text2 = input("Enter some more text to append: ")
with open("output.txt", "a") as file:
    file.write(text2 + "\n")

# Read and display content
print("Final contents of the file:")
with open("output.txt", "r") as file:
    print(file.read())
