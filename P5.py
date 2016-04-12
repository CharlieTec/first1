def absolute(N):
    if N<0:
        return -1 * N
    else:
        return N
print "|-1| =", absolute (-1)
print "|100| =", absolute(100)
print "|0| =", absolute(0)

x = 9
if x<0:
    print 'Negative'
elif x==0:
    print 'Zero'
else:
    print 'Positive'

x=0
if x<0:
    print 'Negative'
elif x==0:
    print 'Zero'
else:
    print 'Positive'

################################## TAX EXAMPLE################
def get_tax_amount(salary):
    if salary<20000:
        return 0
    elif salary>= 20000 and salary<50000:
        return salary*0.15
    elif salary>=50000 and salary<100000:
        return salary*0.20
    else:
        return salary*0.33
print "Bob's Salary 1 = $15,000.00 and Pay Tax = $", get_tax_amount (15000.00)
print "John's Salary 2 = $25,000.00 and Pay Tax = $", get_tax_amount (25000.00)
print "Pete's Salary 3 = $60,000.00 and Pay Tax = $", get_tax_amount (60000.00)
print "Joan's Salary 4 = $150,000.20 and Pay Tax = $", get_tax_amount (150000.20)
print "Charlie's Salary 5 = $250,000.00 and Pay Tax = $", get_tax_amount (250000.00)