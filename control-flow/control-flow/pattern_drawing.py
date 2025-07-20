size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for _ in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after a row
    row += 1
