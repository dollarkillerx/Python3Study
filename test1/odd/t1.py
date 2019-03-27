class Student() :
    c = 2 # class 变量

    def print_file(self) :
        print('hello' + str(self.c))
        self.pr()

    def pr(self) :
        print('123')

student = Student()
student.print_file()