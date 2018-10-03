#execute a set of statmens if condition satisfies
#2. execute set of statments if condition satisfies otherwise execute alternaive set of statements

a=5
b=3
c=2

if a>b:
    print "inside if"
else:
    print "inside else"

if c>b:
    print "inside if"
else:
    print "inside else"


# execute a block of statements based compound/multiple conditions

# cond1 log cond2 log cond3
# cond1 and cond2 or cond3
# a>b and a>c ---> True

if a>b and a>c:
    print "compound"
    print "a is greater"

if c>b and a>c:
    print "compound"
    print "a is greater"


#multiple alternatives

if c>b and a>c:
    print "a is greater"
elif b>a and b>c:
    print "b is greater"
else:
    print "c is greater"

if a>b and a>c:
    print "a is greater"
elif b>a and b>c:
    print "b is greater"
elif c>a and c>b:
    print "c is greater"


#nested if
pin = 5555
amount = 300
avail_amount = 200
if pin == 1234:
    if amount < avail_amount:
        print "You have withdrawn the amount"
    else:
        print "doesn't have sufficient ammount"
else:
    print "in correct pin"

pin = 1234
if pin == 1234 and amount < avail_amount:
    print "You have withdrawn amount"
elif pin != 1234:
    print "incorrect pin"
else:
    print "insufficient balance"
