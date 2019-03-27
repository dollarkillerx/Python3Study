class Test() :
    sums = 12

    def __init__(self,age) :
        self.sums = age
        self.__class__.sums += 16
        print(self.__class__.sums)
        print(self.sums)

test = Test(15)
test1 = Test(15)