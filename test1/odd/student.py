class Student() :
    name = ''
    age = 0
    
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def do_homework(self) :
        print(self.name + 'do homeworld')

    @classmethod
    def plus_sum(cls) :
        print('cls:  ' + cls.name )

    @staticmethod
    def add(x,y):
        print(x + y)

student = Student('dollarkiller',16)

student.do_homework()

Student.plus_sum()

Student.add(16,15)

student.add(16,15)