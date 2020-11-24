class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def name(self):
    return self.firstname + " " + self.lastname

class Student(Person):
    pass # inherit all props from parent


class StudentGraduate(Student):
  def __init__(self, fname, lname, admn_year, grad_year):
    """
    :type admn_year: int
    :type grad_year: int
    """
    super().__init__(fname, lname)
    self.admission_year = admn_year
    self.graduation_year = grad_year

  def years_attended(self):
    return self.graduation_year - self.admission_year
