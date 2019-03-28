import re

a = 'python  1234878 java sdasdsa php golang 48648485'

r = re.findall('[a-z]{3,6}?',a)

print(r)