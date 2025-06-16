
class University:
  def __init__(self, name):
    print("Contructor of the University Class")
    self.name = name 

  def display(self):
    print(f"University : The University name is:  {self.name}")

class Course(University):
  def __init__(self,name,course):
    print("Constructor of the Course Class")
    University.__init__(self,name)
    self.course = course
  def display(self):
    print(f"Course : The Course name is: {self.course} and University name is: {self.name}")
    University.display(self)

class Branch(University):
  def __init__(self,name,branch):
    print("Constructor of the Branch Class")
    University.__init__(self,name)
    self.branch = branch
  def display(self):
    print(f"Branch : The Branch name is: {self.branch} and University name is: {self.name}")
    University.display(self)

class Student(Course, Branch):
  def __init__(self,name,course,branch,student_name):
    print("Constructor of Student Class is called")
    Course.__init__(self,name,course)
    Branch.__init__(self,name,branch)
    self.name = student_name

  def display(self):
    print(f"Student : The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)

ob = Student('Mit','Computer Science','Computer Science and Engineering','John')
ob.display()