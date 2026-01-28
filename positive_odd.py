a = int(input("Enter an integer (positive or negative): "))

if a > 0:
    print(f"The number {a} is positive")
    if a % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif a < 0:
    print(f"The number {a} is negative")
else:
    print(f"The number {a} is zero")

# OUTPUT
Enter an integer (positive or negative): 8
The number 8 is positive
The number is even
