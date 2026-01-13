marks01 = int(input("Enter marks in subject 1: "))
marks02 = int(input("Enter marks in subject 2: "))
marks03 = int(input("Enter marks in subject 3: "))

total_marks_per_subject = 100
total_subjects = 3
total_possible_marks = total_marks_per_subject * total_subjects

# Calculate percentages
subject1_percent = marks01 / total_marks_per_subject * 100
subject2_percent = marks02 / total_marks_per_subject * 100
subject3_percent = marks03 / total_marks_per_subject * 100
overall_percent = (marks01 + marks02 + marks03) / total_possible_marks * 100

# Pass conditions
if subject1_percent >= 33 and subject2_percent >= 33 and subject3_percent >= 33 and overall_percent >= 40:
    print("🎉 You passed the exam!")
else:
    print("❌ You did not pass the exam.")