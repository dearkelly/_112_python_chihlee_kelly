side=int(input('請輸入對邊:'))
another_side=int(input("請輸入斜邊:"))

import math
radian = math.asin(side/another_side)
degree=math.degrees(radian)
print(round(degree,ndigits=2))