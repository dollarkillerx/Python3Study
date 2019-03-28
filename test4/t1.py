# def curve_pre(4) :
#     def cureve(x) :
#         return a*x*x
#     return cureve

# f = curve_pre(16)
# c = f(15)
# print(c)

a = 16
def curve_pre() :
    def cureve(x) :
        return a*x*x
    return cureve

f = curve_pre()
c = f(15)
print(c)