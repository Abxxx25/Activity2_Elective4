# Activity 2: Decision Control Structures
# Prepared by: [Your Name]
# Pangasinan State University

def get_score_input(test_num):
    while True:
        try:
            score = float(input(f"Input score {test_num}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("⚠️ Score must be between 0 and 100. Try again.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number only.")

# Input 5 test scores
scores = []
for i in range(1, 6):
    scores.append(get_score_input(i))

# Compute average
average = sum(scores) / len(scores)
print(f"\nYour Average: {average:.2f}")

# Determine grade based on PSU grading system
if 95 <= average <= 100:
    numerical_rating = "1.0"
    percentage = "95 - 100%"
    remark = "Very Superior"
    letter_grade = "A"
elif 90 <= average <= 94:
    numerical_rating = "1.25 - 1.5"
    percentage = "90 - 94%"
    remark = "Superior"
    letter_grade = "A-"
elif 85 <= average <= 89:
    numerical_rating = "1.75 - 2.0"
    percentage = "85 - 89%"
    remark = "Above Average"
    letter_grade = "B"
elif 80 <= average <= 84:
    numerical_rating = "2.25 - 2.5"
    percentage = "80 - 84%"
    remark = "Average"
    letter_grade = "B-"
elif 75 <= average <= 79:
    numerical_rating = "2.75 - 3.0"
    percentage = "75 - 79%"
    remark = "Passing"
    letter_grade = "C"
else:
    numerical_rating = "5.0"
    percentage = "Below 75%"
    remark = "Failure"
    letter_grade = "C-"

# Display results
print(f"Numerical Rating: {numerical_rating}")
print(f"Percentage Equivalent: {percentage}")
print(f"Adjectival Marks: {remark}")
print(f"Letter Grade: {letter_grade}")
