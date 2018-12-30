#array = re.split(r'        ', line)
#print(array)
import re

array = []
filename = "data"
file = open(filename, "r")
for line in file:
    rx = re.compile(r'\S+ ?\S*')
    array = rx.findall(line)



