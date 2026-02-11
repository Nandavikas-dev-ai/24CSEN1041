numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)

#otuput
Original list: [1, 2, 2, 3, 4, 3, 5, 1, 6]
List without duplicates: [1, 2, 3, 4, 5, 6]
