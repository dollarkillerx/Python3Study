import re

s = 'AB5AS4DG4R8DGRT5GH4F8H48SF5SDF4SD89J5YUK9UIL98'

def conver(value) :
    bbs = value.group()
    if int(bbs) >= 6:
        return '\n'
    

r = re.sub('\d',conver,s)

print(r)