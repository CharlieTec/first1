import math
def cubic (x):
    result=x*x*x
    return result

def cubic2 (x):
    return x*x*x

value1 = cubic(3)
value2 = cubic2(3)



def adder (n1,n2):
    return n1+n2

def test (n1,n2,n3,x):
    result = (n1+n2)/(n3*x)
    return result

def avg_three (n1,n2,n3):
    temp= (n1+n2+n3)/3.0
    return temp
def tan45 (x):
    result= math.tan (x)
    return result




print "Value 1 -", value1
print "Value 2 -", value2

print "adder -", adder (10,1)
print "test -  ",test (5,5,1,5)
print "avg_three - ", avg_three(18,23,19)
print "avg 34,31 28 -", avg_three(34,31,28)
print "tan 45 - ", tan45(0.785398163397)

