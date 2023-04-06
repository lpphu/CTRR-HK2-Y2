# 52100988 Lữ Phúc Phú

''' Exercise 01 '''


import math
from numpy import integer


def isPrime(n):
    if n<2: 
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def nextPrime(n):
    for i in range(n+1,100):
        if isPrime(i):
            return i
        
print(nextPrime(8))

''' Exercise 02 '''
def primeFact(p):
    ans = []
    primeNum = 2
    i = p
    while(i!=1):
        if i%primeNum == 0:
            ans.append(str(primeNum))
            i = i/primeNum
        else:
            primeNum = nextPrime(primeNum)
    return ans
print(str(20) + ' -> ' + ','.join(primeFact(20)))

''' Exercise 03 '''
def printPrime(N):
    ans = []
    for i in range(N+1):
        if isPrime(i):
            ans.append(str(i))
    return ', '.join(ans)
print(printPrime(20))

''' Exercise 04 '''
def ex_04(n): 
    if n<2: 
        return []
    else:
        O = [2]
        i = 3
        while (i+2 < n):
            i += 2
            Flag = True
            j = 0
            while (j+1 < len(O)):
                if i%O[j] == 0:
                    Flag = False
                    break
                j += 1
            if Flag:
                O.append(i)
        return O
    
print(ex_04(20))

''' Exercise 05 '''
# def gcd(a,b):
#     stack = []
#     a1 = primeFact(a)
#     print(a1)
#     b1 = primeFact(b)
#     print(b1)
#     temp = 0
#     while (len(a1) == 0 or len(b1) == 0):
#         tempA = a1.pop()
#         if temp != tempA and temp != 0:
#             a1.insert(0,tempA)
#         tempB = b1.pop()
#         if temp != tempB and temp != 0:
#             b1.insert(0,b1)
#         if tempA == tempB:
#             stack.append(tempA)
#         print(type(tempB))
#         if tempA > tempB:
#             temp = tempA
#         else:
#             temp = tempB
#     while len(a1) != 0:
#         if temp == a1.pop():
#             stack.append(temp)
#     while len(b1) != 0:
#         if temp == b1.pop():
#             stack.append(temp)
#     return stack
def gcd(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
             
    return gcd
print(gcd(3,6))

''' Exercise 06 '''
def lcm(a, b):
    if a > b:
       greater = a
    else:
       greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
        greater += 1
    return lcm
print(gcd(45,72)*lcm(45,72)==45*72)

''' Exercise 07 '''
def DecToBin(n):
    if n == 0:
        return 0
    if n%2 == 0:
        return DecToBin(n//2)*10
    else:
        return DecToBin(n//2)*10 + 1
    
print(DecToBin(15))

''' Exercise 08 '''
def FractionToBin(n):
    if math.isclose(n*2,1):
        return '1'
    if abs(n*2) > 0:
        return '0' + FractionToBin(n*2)
    else:
        return '1' + FractionToBin(n*2)
def FloatToBin(n):
    intValue = math.floor(n)
    floatValue = n - intValue
    ans = str(DecToBin(intValue)) + '.' + str(FractionToBin(floatValue))
    return float(ans)
print(FloatToBin(5.25))

''' Exercise 09 '''
def Hex(n):
    match(n):
        case 0:
            return '0'
        case 1:
            return '1'
        case 2:
            return '2'
        case 3:
            return '3'
        case 4:
            return '4'
        case 5:
            return '5'
        case 6:
            return '6'
        case 7:
            return '7'
        case 8:
            return '8'
        case 9:
            return '9'
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'
def DecToHex(n):
    if n == 0:
        return '0'
    if n < 16:
        return Hex(n%16)
    return DecToHex(n//16) + Hex(n%16)
    
print(DecToHex(47))

''' Exercise 10 '''
def convertBase(a,base1,base2):
    a = list(a)
    temp = int(''.join([str(i) for i in a]))
    if base1 == 10 and base2 == 2:
        return [i for i in str(DecToBin(temp))]
    if base1 == 10 and base2 == 16:
        return [i for i in str(DecToHex(temp))]
    
print(convertBase([1,1,1],10,16))






