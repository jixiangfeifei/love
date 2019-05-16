#用for 实现0到100之间的偶数求和

num = 0
for i in range(0,101,2):
    num += i
print (num)

#---------------

#用while 实现猜数字游戏

import random

answer = random.randint(0,100)
num = 0
while True:
    num += 1
    number = int(input("在0和100之间猜一个数字："))
    if number > answer:
        print ("大了！")
    elif number < answer:
        print  ("小了！")
    else:
        print ("答对了！")
        break
if num > 7:
    print ("你好笨了")
elif num < 7:
    print ("你好聪明")

#-----------------
#九九乘法口诀表

for i in range(1,10):
    for j in range(1,i+1):
        print ("%d * %d = %d"%(j,i,i*j),end="\t")         #\t 表示制表符，tab 的宽度
    print()


