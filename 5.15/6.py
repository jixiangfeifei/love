# 输入月收入和五险一金 计算个人所得税

salary = float(input("月收入："))
insurance = float(input("五险一金："))
diff = salary - insurance -3500

if diff <= 0:
    rate = 0
    deduction = 0
if diff < 1500:
    rate = 0.03
    deduction = 0
if diff < 4500:
    rate = 0.1
    deduction = 105
if diff < 9000:
    rate = 0.2
    deduction = 555
if diff < 35000:
    rate = 0.25
    deduction = 1005
if diff < 55000:
    rate = 0.3
    deduction = 2755
if diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505

tax = abs(diff * rate - deduction)
print ("个人所得税: %.3f 圆" % tax)
print ("实际到手收入：%.f 圆" %(diff +3500 -tax))


