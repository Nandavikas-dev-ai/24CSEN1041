# List of student marks
marks = [78, 85, 62, 90, 88, 76, 95, 69]

# Calculate average
average = sum(marks) / len(marks)

# Highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Count how many students scored above average
count_above_avg = 0
for mark in marks:
    if mark > average:
        count_above_avg += 1

# Display results
print("Average mark:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Number of students above average:", count_above_avg)

#output
Average mark: 80.375
Highest mark: 95
Lowest mark: 62
Number of students above average: 4
