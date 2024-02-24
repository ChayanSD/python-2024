# Problem: Assign a letter grade based on a student's 
#score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score:"))
if score >= 101:
    print("Invalid score")
    exit()
    
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Your grade is : {grade}")