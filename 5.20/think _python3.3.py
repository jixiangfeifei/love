def print_cat(s):
    ls = len(s)
    print(" "*(70-ls),s)

sc = "t5wgf"

print_cat(sc)
#----------------------------------------


def do_twice(f,d):
    f(d)
    f(d)


def print_spam(ww):
    print (ww)


do_twice(print_spam,"er")

zx = print_spam
def do_fourc(es,a):
    do_twice(es,a)
    do_twice(es,a)

do_fourc(zx,'ert34')
print(type(print_spam))


#----------------------------------------

def print1(a,b,c):
    print(a+b*c+a+b*c+a)


def print2(e):
    e
    e
    e
    e

print1('+',5,'-')
print1('|',5,' ')
print1('|',5,' ')
print1('|',5,' ')
print1('|',5,' ')
print1('+',5,'-')