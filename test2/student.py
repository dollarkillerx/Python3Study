from human import Human

class Student(Human) :

    def __init__(self,name):
        self.name = name

    def do_homework(self) :
        print(self.name + 'do homework')

student1 = Student('dollarkiller')
student1.get_name()
student1.do_homework()

print(Student.sum)