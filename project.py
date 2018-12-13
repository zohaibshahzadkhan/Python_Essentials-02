# Assume you are a teacher of a class write a python program to 
# 1) Read the name and total marks score by students of your class atleast 3 or more students 
# 2) Rank the students 
# 3) Give reward to top 3 students 

import operator;

def readStudentDetail():
  print("Enter the number of the students ")
  numberOfStudents = int(input());
  studentRecord = {}
  for student in range(0,numberOfStudents):
    print("Enter the name of the student");
    name = input();
    print("Enter the marks of the student");
    marks = int(input());
    studentRecord[name] = marks;
  return studentRecord;

def rankStudents(studentRecord):
  sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
  count = 1;
  for student in sortedStudentRecord:
    if count < 4: 
      print("{} has scored {} rank, scoring {} marks".format(student[0], count , student [1]));
      count = count + 1;
    else:
      break;
  return sortedStudentRecord;

def rewardStudents(sortedStudentRecord, reward):
  count = 0;
  for students in sortedStudentRecord:
    if count < 3:
      print("{} has recieved a cash reward of {}".format(students[0], reward[count]))
      count= count + 1;
    else:
      break;
  

# def appriciateStudents():

studentRecord = readStudentDetail();
sortedStudentRecord = rankStudents(studentRecord);
reward = (500, 300, 200);
rewardStudents(sortedStudentRecord, reward);
