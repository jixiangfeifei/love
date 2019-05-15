#掷塞子来决定做什么

from random import randint

face = randint (1,6)

if face == 1:
    print ("sing a song")
elif face == 2:
    print ("smale")
elif face == 3:
    print ("学狗叫")
elif face == 4:
    print ("做虎卧撑")
elif face == 5:
    print ("讲个笑话")
else:
    print ("肩倒立")

