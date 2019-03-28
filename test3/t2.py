import re

a = '2C|5C++|J9AVA|C#5|PHP|4PYTHON|5JS|T2S'

r = re.findall('\d',a)

ra = re.findall('\D',a)

print(r)

print(ra)