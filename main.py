
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
  grade = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  print(f"Grade point for course 1 is: {getGradePoint(grade)}")

  grade = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  print(f"Grade point for course 2 is: {getGradePoint(grade)}")

  grade = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  print(f"Grade point for course 3 is: {getGradePoint(grade)}")
  
  GPAcalculation = ((grade * credit1 + grade * credit2 + grade * credit3) / (credit1 + credit2 +credit3))
  print(f"Your GPA is: {GPAcalculation}")

if __name__ == "__main__":
  run()