#百分制成绩转登记制

score = eval(input("输入成绩"))
sd = "成绩"
if score >= 90:
    print (sd ,"是 A")
elif 80 <=score <90:
    print (sd +"是 B")
elif 70 <= score <80:
    print (sd ,"是 C")
elif 60<= score <70:
    print (sd ,"是 D "  )
else :
    print (sd, "是 E")

