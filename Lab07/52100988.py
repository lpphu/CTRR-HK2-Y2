# 52100988 Lữ Phúc Phú

''' Exercise 01 '''
from math import comb


print("1.")
def thieves(x):
    if x == 1:
        return 1
    return thieves(x-1) + x

# ''' Exercise 02 '''
# print("2.")
# def richest(x,n):
#     if n == 1:
#         return x

''' Exercise 03 '''
print("3.")

def waytochoose(n,k):
    if k==0 or k==n:
        return 1
    return waytochoose(n-1,k) + waytochoose(n-1,k-1)
for i in range(50+1):
    ways = waytochoose(50,i)
    if 
    
print(waytochoose(50,1000))

