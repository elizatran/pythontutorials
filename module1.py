from tempconv import ctof
from tempconv import ftoc
temp = 212
convTemp = ftoc(temp)
print('The converted temp is ' + str(convTemp))
temp = 0
convTemp = ctof(temp)
print('The converted temp is ' + str(convTemp))

import hinh
s1 = hinh.Shape(4,8)
print(s1)
r1 = hinh.Rectangle (5,10,6,9)
print(r1)