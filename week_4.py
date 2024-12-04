"""
- File Read & Write Challenge: Create a program that reads a file and writes a modified version to a new file.
- Error Handling Lab: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

Learning Outcomes:
I will be skilled in managing files efficiently in Python, ensuring error-free code that gracefully handles unexpected issues. Mastering files and exception handling will allow you to build strong, robust applications!
"""
try:
    # Prompt the user to enter a filename.
    file_name = input("Enter a name of your file to read: ")
    
    # Open the file in read mode.
    with open(file_name, 'r') as file:
        data = file.read()
        
        # Print the contents of the file.
        print(data)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
