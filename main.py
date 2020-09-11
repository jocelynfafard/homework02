
def getGradePoint(grade):

  if lettergrade1 == "A":
    gradepoint1 = 4.0;
  elif lettergrade1 == "A-":
    gradepoint1 = 3.67;
  elif lettergrade1 == "B+":
    gradepoint1 = 3.33;
  elif lettergrade1 == "B":
    gradepoint1 = 3.0;
  elif lettergrade1 == "B-":
    gradepoint1 = 2.67;
  elif lettergrade1 == "C+":
    gradepoint1 = 2.33;
  elif lettergrade1 == "C":
    gradepoint1 = 2.0;
  elif lettergrade1 == "D":
    gradepoint1 = 1.0;
  elif lettergrade1 == "F":
    gradepoint1 = 0.0;
  else:
    gradepoint1 = 0.0;



def run():
  lettergrade1 = input("Enter your course letter grade: ")
  credit1 = input("Enter your course credit: ")
  credit1 = float(credit1);
  print(f"Grade point for course 1 is: {getGradePoint(grade)}")

  lettergrade2 = input("Enter your course letter grade: ")
  credit2 = input("Enter your course credit: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2 is: {getGradePoint(grade)}")

  lettergrade3 = input("Enter your course letter grade: ")
  credit3 = input("Enter your course credit: ")
  credit3 = float(credit3);
  print(f"Grade point for course 3 is: {getGradePoint(grade)}")
  
  GPAcalculation = ((gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 +credit3))
  print(f"Your GPA is: {GPAcalculation}")