import re

lanuage = 'PythionC#\nJavaC#Php'

# r = re.sub('C#','GO',lanuage,1)

# print(r)

def convert(value) :
    return 'GOlang'

r = re.sub('C#',convert,lanuage,1)

print(r)