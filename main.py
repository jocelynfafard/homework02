
def getGradePoint(grade):

  if grade == "A":
    return 4.0;
  elif grade == "A-":
    return 3.67;
  elif grade == "B+":
    return 3.33;
  elif grade == "B":
    return 3.0;
  elif grade == "B-":
    return 2.67;
  elif grade == "C+":
    return 2.33;
  elif grade == "C":
    return 2.0;
  elif grade == "D":
    return 1.0;
  elif grade == "F":
    return 0.0;
  else:
    return 0.0;

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  gradepoint1 = getGradePoint(grade1)
  print(f"Grade point for course 1 is: {gradepoint1}")

  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  gradepoint2 = getGradePoint(grade2)
  print(f"Grade point for course 2 is: {gradepoint2}")

  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  gradepoint3 = getGradePoint(grade3)
  print(f"Grade point for course 3 is: {gradepoint3}")
  
  GPAcalculation = ((gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 +credit3))
  print(f"Your GPA is: {GPAcalculation}")

if __name__ == "__main__":
  run()