
def getGradePoint(grade):

if lettergrade1 == "A":
  gradepoint1 = 4.0;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "A-":
  gradepoint1 = 3.67;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "B+":
  gradepoint1 = 3.33;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "B":
  gradepoint1 = 3.0;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "B-":
  gradepoint1 = 2.67;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "C+":
  gradepoint1 = 2.33;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "C":
  gradepoint1 = 2.0;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "D":
  gradepoint1 = 1.0;
  print(f"Grade point for course 1 is: {gradepoint1}")
elif lettergrade1 == "F":
  gradepoint1 = 0.0;
  print(f"Grade point for course 1 is: {gradepoint1}")
else:
  gradepoint1 = 0.0;
  print(f"Grade point for course 1 is: {gradepoint1}")

lettergrade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)
if lettergrade2 == "A":
  gradepoint2 = 4.0;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "A-":
  gradepoint2 = 3.67;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "B+":
  gradepoint2 = 3.33;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "B":
  gradepoint2 = 3.0;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "B-":
  gradepoint2 = 2.67;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "C+":
  gradepoint2 = 2.33;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "C":
  gradepoint2 = 2.0;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "D":
  gradepoint2 = 1.0;
  print(f"Grade point for course 2 is: {gradepoint2}")
elif lettergrade2 == "F":
  gradepoint2 = 0.0;
  print(f"Grade point for course 2 is: {gradepoint2}")
else:
  gradepoint2 = 0.0;
  print(f"Grade point for course 2 is: {gradepoint2}")

lettergrade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3);
if lettergrade3 == "A":
  gradepoint3 = 4.0;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "A-":
  gradepoint3 = 3.67;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "B+":
  gradepoint3 = 3.33;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "B":
  gradepoint3 = 3.0;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "B-":
  gradepoint3 = 2.67;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "C+":
  gradepoint3 = 2.33;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "C":
  gradepoint3 = 2.0;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "D":
  gradepoint3 = 1.0;
  print(f"Grade point for course 3 is: {gradepoint3}")
elif lettergrade3 == "F":
  gradepoint3 = 0.0;
  print(f"Grade point for course 3 is: {gradepoint3}")
else:
  gradepoint3 = 0.0;
  print(f"Grade point for course 3 is: {gradepoint3}")


def run():
lettergrade1 = input("Enter your course letter grade: ")
  credit = input("Enter your course credit: ")
  credit = float(credit);
  getGradePoint(grade);

GPAcalculation = ((gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 +credit3))
print(f"Your GPA is: {GPAcalculation}")