# 判断输入的边长能否构成三角形
# 如果构成三角形，则计算出三角形的面积和周长

import math

a = float (input ("边长a="))
b = float (input ("边长b="))
c = float (input ("边长c="))

if a + b >c  and a +c >b and b + c >a :
    print ("周长: %.3f" %(a+b+c))
    p = (a + b + c)/2
    arer = math.sqrt(p * (p - a)*(p - b)*(p - c))
    print ("面积：%f" %(arer))

else:
    print ("不能构成三角形")
