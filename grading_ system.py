# Grading system based on score

# Get user input
score = int(input("Enter your score (0-100): "))

# Determine the grade
if 70 <= score <= 100:
    grade = "A"
elif 60 <= score <= 69:
    grade = "B"
elif 50 <= score <= 59:
    grade = "C"
elif 45 <= score <= 49:
    grade = "D"
elif 40 <= score <= 44:
    grade = "E"
elif 0 <= score < 40:
    grade = "F"
else:
    grade = "Invalid score. Please enter a number between 0 and 100."

# Print result
print("Your grade is:", grade)