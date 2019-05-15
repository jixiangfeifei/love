# 从任意长度的可迭代对象中分解元素

record = (3234,"wefe",563546,4,'gwert',65,35463546,)
sdf ,er, *number = record

print (*number)

er3 , *number ,gd = record

print (*number)

# -------------------

def drop_first_last(grades):
    first,*middle,last = grades
    return (middle)
dd = [332,343,345,'dsfg','eqwe','35qwer','3324',23423,445,'4324',341234,'drfwe',3423]


print (drop_first_last(dd))


#---------------------

records = [('foo',1,2),('bar','hellow'),('foo',3,4)]

def do_foo(x,y):
    print ('foo',x,y)

def do_bar(s):
    print ('bar',s)

for tag ,*args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
