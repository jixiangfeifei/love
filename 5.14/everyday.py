#练习1:将华氏温度转为摄氏温度

f = float(input ("请输入华氏温度"))

c = (f -32)/1.8

print ("摄氏温度是", c)
print ('%.1f华氏温度 = %.1f摄氏温度'%(f,c))


#练习2:输入圆的半径，求出面积和周长

import math
r = eval(input ("输入半径"))

area = math.pi * r **2
perimater = 2 * math.pi * r

print ("圆的面积是 %.3f , 周长是 %.3f"%(area,perimater))

#练习3：输入年份判断是否闰年

year = int (input("请输入年份"))

yesyear = year % 4 == 0 and \
    year %100 != 0  or year % 400 ==0

print (yesyear)

