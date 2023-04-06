# 52100988 Lữ Phúc Phú  

' ' ' Exercise01 ' ' '
from math import *
import random


print("1.")
# a.
P = 'Phong has Visa'
S1 = 'If phong can fly, Phong will go to America'
S2 = 'If Phong has Visa, Phong will go to America'
S3 = 'If Phong can speak English, Phong will go to America'
C = 'Phong goes to America'

print("a.")
print("P and S2 -> C")
print("P: %s"%(P))
print("S2: %s"%(S2))
print("C: %s"%(C))

# b.
P = "It's hot yesterday"
S1 = "If it's hot, it will rain the next day"
S2 = "If and only if it's not rain, Nam goes outside"
S3 = "If it's not hot, Nam will go outside"
C = "Nam goes outside"

print("b.")
print("P and S2 -> C")
print("P: %s"%(P))
print("S2: %s"%(S2))
print("C: %s"%(C))

# c.
Q = "An wake up late"
R = "The traffic is flowing smooth"
S1 = "The traffic is always heavy on school day"
S2 = "If An wake up late, he will be late for school on school day"
S3 = "An only have to go to school in school day"
S4 = "If An don't have to go to sachool, An can't be late for school"
C = "An is late for school"

print("c.")
print("Q, R and S2 -> C")
print("P: %s"%(P))
print("S2: %s"%(S2))
print("C: %s"%(C))

# d.
P ="∃x, y ∈ R,(x + y)^2 ≤ x^2 + y^2"
Q ="∀x, y ∈ Z+, x + y ≥ x + y"
R ="∀x, y ∈ Z+, x + y + 2√(xy) ≥ x + y"
T ="∀x, y ∈ Z+,√(x + y) ≥ 0"
S1 ="∀x, y ∈ Z+, x^2 ≥ y^2 → x ≥ y"
S2 ="∀x, y ∈ Z+, x ≥ y → x^2 ≥ y^2"
S3 ="∀x, y ∈ R+, x ≥ y → x^2 ≥ y^2"
S4 ="∀x, y ∈ R+, x^2 ≥ y^2 → x ≥ y"

print("d.")
print("P, Q, R, T and S2 -> C")
print("P: %s"%(P))
print("S1: %s"%(S1))
print("C: %s"%(C))

' ' ' Exercise02 ' ' '
print("2.")
# a.
print("a. ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 15^2 + 16^2")
count = []
for i in range(100+1):
    if i**2 == 15**2 + 16**2:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", count)

# b.
print("b. ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2")
count = []
for i in range(100+1):
    if i**2 == 12**2 + 16**2:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

# c.
print("c. ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99x")
count = []
for i in range(-50,51):
    if i**2 >= 99*i:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

# d.
print("d. ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0")
count = []
for i in range(50,100+1):
    if i*(i+1)*(i+2)%6 != 0:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

# e.
print("e. ∃x, y ∈ Z, 0 ≤ x ≤ 100,√(x + y) = √x + √y")
count = []
for i in range(100+1):
    for j in range(100+1):
        if sqrt(i+j) == sqrt(i) + sqrt(j):
            count.append([i,j])
if len(count) == 0:
    print("the given statement is incorrect for all values x and   within the given domain.")
else:
    print("the given statement is correct when x and y equal to", random.choice(count))

' ' ' Exercise03 ' ' '
# a.
print("a. Negated statement: !∀x ∈ Z, 0 ≤ x ≤ 100, x^3 >= x")
count = []
for i in range(100+1):
    if i**3 >= i:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

def prime_number(n):
    if n<2:
        return False
    if n==2: 
        return True
    for i in range(2,n):
        if n%2==0:
            return False
    return True
# b.
print("b. Negated statement: !∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x ∗ 3 + 1 is a prime number")
count = []
for i in range(100+1):
    if i%2== 0 and prime_number(i*3+1):
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

# c.
print("c. Negated statement: !∀x ∈ Z, 1 ≤ x, y ≤ 100, and x is even, x ∗ 5 + 3 is a prime number")
count = []
for i in range(1,100+1):
    if i%2== 0 and prime_number(i*5+3):
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values x within the given domain.")
else:
    print("the given statement is correct when x equal to", random.choice(count))

# d.
print("d. Negated statement: !∀c ∈ Z, 0 < c ≤ 100, c%4 = 0, !∃a, b ∈ Z+, c2 = a^2 + b^2")
count = []
for c in range(1,100+1):
    if c%4==0:
        for a in range(100):
            for b in range(100):
                if c**2 == a**2 + b**2:
                    count.append([c,[a,b]])
if len(count) == 0:
    print("the given statement is incorrect for all values c within the given domain.")
else:
    print("the given statement is correct when c, a and b equal to", random.choice(count))

# e.
print("e. Negated statement: !∀c ∈ Z, 0 < c ≤ 100, c%5 = 0, !∃a, b ∈ Z+, c^2 = a^2 + b^2")
count = []
for c in range(1,100+1):
    if c%c==0:
        for a in range(100):
            for b in range(100):
                if c**2 == a**2 + b**2:
                    count.append([c,[a,b]])
if len(count) == 0:
    print("the given statement is incorrect for all values c within the given domain.")
else:
    print("the given statement is correct when c equal to", random.choice(count))

# f.
print("f. Negated statement: !∃c ∈ Z, 0 < c ≤ 100, c^2 ≤ c")
count = []
for i in range(1,100+1):
    if i**2 <= i:
        count.append(i)
if len(count) == 0:
    print("the given statement is incorrect for all values c within the given domain.")
else:
    print("the given statement is correct when c equal to", random.choice(count))

' ' ' Exercise04 ' ' '
print("4.")
# a.
print("a.")
count = []
for i in range(10+1):
    for j in range(10+1):
        if pow((i+j),2) > pow((i+2*j),2):
            count.append([i,j])
if len(count) == 0:
    print("the given statement is incorrect for all values x and y within the given domain.")
else:
    print("the given statement is correct when x and y equal to", random.choice(count))

# b.
print("b.")
count = []
for i in range(10+1):
    if factorial(20) < factorial(i):
        count.append([i])
if len(count) == 0:
    print("the given statement is incorrect for all values x and y within the given domain.")
else:
    print("the given statement is correct when x and y equal to", random.choice(count))

# c.
print("c.")
count = []
for i in range(10+1):
    if 3*i**2 >= 10**3:
        count.append([i])
if len(count) == 0:
    print("the given statement is incorrect for all values x and y within the given domain.")
else:
    print("the given statement is correct when x and y equal to", random.choice(count))

# d.
print("c.")
count = []
for i in range(10+1):
    if (4*i**3 + 6*i**2 + 2*i) > 10**4 + 2*10**3 + 10**2 - 5**4 - 2*5**3 - 5**2:
        count.append([i])
if len(count) == 0:
    print("the given statement is incorrect for all values x and y within the given domain.")
else:
    print("the given statement is correct when x and y equal to", random.choice(count))

' ' ' Exercise05 ' ' '
print("5.")
# a.
print("a.")
G1 = "p -> r"
G2 = "~p -> q"
G3 = "q -> s"
G4 = ""

#a
print('a.')
G1 =  'p -> r'
G2 = ' ~p -> q '
G3 = ' q -> s'
G4 = ' G3 ' + '+' + G2 + "->" + '~p -> s ( transitivity) '
G5 = G1 + '->' + '~r -> ~q' + '(contrapositive)'
C = G4 +"+"+ G5 + "~r -> s" + "( transitivity)"
print("G1=",G1)
print("G3=",G3)
print("G4=",G4)
print("G5=",G5)
print("C=",C)

#b
print('b.')
G1 =  'p -> r'
G2 = ' ~r v s '
G3 = 'p v s '
G4 =  G3 + '->' + '~p -> r ( if then laws) '
G5 =  G2 + '->' + 'r -> s(if then laws)'
G6 = G1 + '->' + '~q -> ~p (contrapositive)'
G7 = G4 + '+' + G5 + '->' + '~p -> s (transitivity)'
C = G7 +"+"+ G6 + "~q -> s" + "( transitivity)"
print("G1=",G1 )
print("G3=",G3)
print("G4=",G4 )
print("G5=",G5 )
print("G6=",G6 )
print("G7=",G7 )
print("C=",C )

#c
print('c.')
G1 =  'p -> ( q -> r )'
G2 = ' p v s  '
G3 = '  t -> q  '
G4 = ' ~s '
G5 =  G2 + '+' + G4 + '->' +  'p (elimination)'
G6 = G1 + '+' + G5 + '->' + 'q -> r (modus Ponens)'
G7 = G6 + '+' + G3 + '->' + 't -> r ( transitivity)'
C = G7 + '->' + '~r -> ~t (contrapositive)'
print("G1=",G1 )
print("G3=",G3)
print("G4=",G4 )
print("G5=",G5 )
print("G6=",G6 )
print("G7=",G7 )
print("C=",C )

#d
print('d.')
G1 =  ' p '
G2 = ' p -> r '
G3 = 'p -> ( q v ~r) '
G4 = '~q v ~s'
G5 =  G2 + '+' + G1 + '->' + 'r (modus ponens)'
G6 = G3 + '+' + G5 + '->' + ' q V ~r (modus ponens)'
G7 = G6 + '+' + G5 + '->' + 'q elimination' 
C = G4 +"+"+ G7 + "s" + "( elimination)"
print("G1=",G1 )
print("G3=",G3)
print("G4=",G4 )
print("G5=",G5 )
print("G6=",G6 )
print("G7=",G7 )
print("C=",C )






