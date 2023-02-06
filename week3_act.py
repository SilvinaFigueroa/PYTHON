

#Create a different version of the program that:

#Calculates the overall grade for four equally weighted programming assignments, 
# in which each assignment is graded out of 50 points. 
# Hint: First calculate the percentage for each assignment (e.g., score / 50), 
# then calculate the overall grade percentage (be sure to multiply the result by 100).
#Calculates the overall grade for four equally weighted programming assignments,
# in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 
# are graded out of 75 points.
#Calculates the overall grade for a course with three equally 
# weighted exams (graded out of 100 points) that account for 60% of the overall 
# grade and four equally weighted programming assignments (graded out of 50 points) that account for
#  40% of the overall grade. 
# Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.

    
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

overall_grade = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f'Your overall grade is: {overall_grade}')

