# 52100988 Lữ Phúc Phú  
from math import sqrt

' ' ' Exercise01 ' ' '
print("1.")
print("a. P -> Q ^ Q -> P")
print("b. P ^ ~Q")
print("c. Q v P")

' ' ' Exercise02 ' ' '
print("2.")
print("a. If P then Q and if Q then P")
print("a. If P then ~Q")
print("a. If Q then P")

' ' ' Exercise03 ' ' '
# chưa làm
print("3.")
print("a. P -> Q v (Q -> P)")

' ' ' Exercise04 ' ' '
print("4.")
print("a.")
p="Phong has Visa" 
q="Phong can fly" 
r="Phong can speak English" 
t="Phong goes to america"
P ="Phong has Visa"
S1="If Phong can fly, Phong will go to America"
S2="If Phong has Visa, Phong will go to America"
S3="If Phong can speak English, Phong will go to America"

P = "p"
S1 = "q -> t"
S2 = "p -> t"
S3 = "r -> t"
C = "t"

print ("%s\n%s\n%s\n.%s"%(S1 , S2 , S3, C ))

print("b.")
p ="An wake up late"
q ="the traffic is flowing smooth"
# ~q ="the traffic is heavy"
r ="school day"
s ="An have go to school"
v ="An is late for school"

P ="An wake up late"
Q ="The traffic is flowing smooth"
S1="The traffic is always heavy on school day"
S2="If An wake up late, he will be late for school on school day"
S3="An only have to go to school on school day"
S4="If An don’t have to go to school, An can’t be late for school"

P = "p"
Q = "q"
S1 = "q -> t"
S2 = "p -> t"
S3 = "r -> t"
S4 = "~s -> ~v"
C = "t"

print ("%s\n%s\n%s\n.%s"%(S1 , S2 , S3, C ))

' ' ' Exercise06 ' ' '


print("6.")
A=[
[2 ,0 ,5 ,0 ,3 ,0],
[3 ,0 ,0 ,0 ,0 ,0],
[0 ,6 ,2 ,0 ,5 ,0],
[3 ,0 ,9 ,0 ,25 ,0],
[0 ,0 ,2 ,4 ,5 ,0],
[0 ,0 ,0 ,0 ,0 ,5]
]

def Implies(p,q):
    if p:
        return q
    else:
        return True

def And(p,q):
    if p==True and q==True:
        return True
    else:
        return False

def Or(p,q):
    if p==True or q==True:
        return True
    else:
        return False

def Not(p):
    if p==True:
        return False
    else:
        return True

def isOdd(a):
    if a%2==0:
        return True
    return False

def isPrime(a):
    if a<2:
        return False
    if a==2:
        return True
    for i in range(2,a):
        if a%2==0:
            return False
    return True

def isSquare(a):
    if a == pow(int(sqrt(a)),2):
        return True
    return False

def isGreater(a,b):
    return a>b

def isEqual(a,b):
    return a==b

def isAbove(a,b):
    row_a = []
    row_b = []
    row = 1
    for i in A:
        for j in i:
            if a == j:
                row_a.append(row)
            if b == j:
                row_b.append(row)
        row += 1
    if i in row_a > j in row_b:
        return True
    return False
    
def isLeftOf(a,b):
    col_a = []
    col_b = []
    for i in A:
        col = 1 
        for j in i:
            if a == j:
                col_a.append(col)
            if b == j:
                col_b.append(col)
            col += 1
        if i in col_a > j in col_b:
            return True
    return False

aa = []
for i in A:
    for j in i:
        aa.append(And(Not(j),isPrime(j)))
if True in aa:
    print("a. True")
else:
    print("a. False")

b = []
for i in A:
    for j in i:
        b.append(Implies(isOdd(j),isSquare(j)))
if False not in b:
    print("b. True")
else:
    print("b. False")

c = []
for i in A:
    for j in i:
        c.append(Implies(isOdd(j),isGreater(j,2)))
if False not in c:
    print("c. True")
else:
    print("c. False")      

d = []
for i in A:
    for j in i:
        d.append(Implies(isPrime(j),Not(Or(isGreater(j,3),isEqual(j,3)))))
if True in d:
    print("d. True")
else:
    print("d. False")

e = []
for i in A:
    for j in i:
        for k in A:
            for l in k:
                e.append(isLeftOf(j,l))
if True in e:
    print("e. True")
else:
    print("e. False")

f = []
for i in A:
    for j in i:
        for k in A:
            for l in k:
                e.append(Implies(isGreater(j,l),Not(isAbove(j,l))))
if True in f:
    print("f. True")
else:
    print("f. False")

g = []
for i in A:
    for j in i:
        for k in A:
            for l in k:
                g.append(Implies(And(And(isPrime(j),Not(isOdd(j))),isOdd(l)),isAbove(j,l)))
if False not in g:
    print("g. True")
else:
    print("g. False")

h = []
for i in A:
    for j in i:
        for k in A:
            for l in k:
                h.append(Implies(And(And(And(isSquare(j),Not(isOdd)),Not(isOdd(l))),Not(isEqual(j,l))),isLeftOf(l,j)))
if False not in h:
    print("h. True")
else:
    print("h. False")
