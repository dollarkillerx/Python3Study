import re

a = 'PythonPythnoPythonpPythonPythonPythonPythonPython'

r = re.findall('(Python){3}',a)

print(r)