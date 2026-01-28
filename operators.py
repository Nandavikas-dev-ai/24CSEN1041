a = 10
b = 20

# Arithmetic Operators
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}\n")

# Relational Operators
print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical Operators
print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")

# Conditional (Ternary) Operator
print("\n" + ("a is greater than b" if a > b else "b is less than a"))

# OUTPUT
Arithmetic Operators
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = 0.50
10 % 20 = 10

Relational Operators
10 < 20 = True
10 > 20 = False
10 == 20 = False
10 != 20 = True

Logical Operators
AND 10 and 20 = True
OR 10 or 20 = True
NOT 10 = False

Bitwise Operators
10 & 20 = 0
10 | 20 = 30
Bitwise XOR 10 ^ 20 = 30
Left Shift 10 << 2 = 40
Right Shift 10 >> 2 = 2

b is less than a
