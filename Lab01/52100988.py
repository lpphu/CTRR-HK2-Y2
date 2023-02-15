# Exercises 1
print("1.")

print("a." , 15*2+7*8)

print("b.",20-15+15*2)

print("c.", 20+30-3*15+5*5**2)

print("d.", (4/6+2/6)/(5/2+1/2))

print("e.", 14/2 + 7)

print("f.", (5*2)/(5-20*3**2+30))

# Exercises 2
print("2.")

print("a. 15*2+7*8 =" , 15*2+7*8)

print("b. 20-15+15*2 =",20-15+15*2)

print("c. 20+30-3*15+5*5**2 =", 20+30-3*15+5*5**2)

print("d. (4/6+2/6)/(5/2+1/2) =", (4/6+2/6)/(5/2+1/2))

print("e. 14/2+7 =", 14/2 + 7)

print("f. (5*2)/(5-20*3**2+30) =", (5*2)/(5-20*3**2+30))

# Exercises 3
print("3.")
def sumN(n):
    s = 0
    for i in range(n+1):
        s+=i
    if n < 0:
        s*=-1
    return s

print(sumN(1))

# Exercises 4
print("4.")

str = input("Enter your string:")

print("a.",str.replace(" ",""))
print("b.",str.replace(" ","_"))

# Exercises 8
print("8.")

def mySum(a, b):
    return a+b
def mySub(a, b):
    return a-b
def myMul(a, b):
    return a*b
def myDiv(a, b):
    return a/b
def myPow(a, b):
    return a**b
dic = {'+':mySum, '-':mySub, '*':myMul, '/':myDiv, '^':myPow}


# Exercises 7
print("7.")
def triangleEx07(n):
    star = ""
    for i in range(n):
        star = "*"*(i+1)
        print(star)
        star = ""

# Exercises 8
print("8.")
def triangleEx08(n):
    star = ""
    for i in range(n):
        star = " "*(i) + "*"*(n-i)
        print(star)
        star = ""


# Exercises 9
print("9.")
def triangleEx09(n):
    star = ""
    for i in range(n):
        star = " "*(n-i-1) + "*"*(2*i+1)
        print(star)
        star = ""

# Exercises 10
print("10.")
def triangleEx10(n):
    star = ""
    for i in range(n):
        star = " "*(i) + "*"*(2*n-2*i-1)
        print(star)
        star = ""

triangleEx09(3)




