' ' ' Exercise01 ' ' '
from re import search


print("1.")
print("a. =====")
print("D is 'all fishes'")
print("P is 'need water to survive'")
print("Formal form: For all x in D, P(x)")

print("b. =====")
print("D is 'a person'")
print("P is 'is left handed'")
# print("Formal form: Exits x in D, P(x)")

print("c. =====")
print("D is 'an employee in the company'")
print("P is 'is late to work everyday'")

print("d. =====")
print("D is 'all fishes in this pond'")
print("P is 'are Koi fish'")

print("e. =====")
print("D is 'creature in the ocean'")
print("P is 'can live on land'")

print("f. =====")
print("D is 'students in class A'")
print("P is 'did not pass the test'")

' ' ' Exercise02 ' ' '
print("2.")
def formalConvert(S):
    temp = str(S).split(',')
    D = temp[0].strip()
    P = ''
    if search("For all", D):
        D = D.replace('For all','')
        P = ' '.join(temp[1].strip().split()[1:])
    if search("Exist", D):
        D = D.replace('Exist','')
        P = ' '.join(temp[1].strip().split()[1:])
    if search('There is at least one', D):
        D = D.replace('There is at least one','')
        P = ' '.join(temp[1].strip().split()[1:])
    return [D,P]

print(formalConvert('For all all fishes, they need water to survive'))

' ' ' Exercise03 ' ' '
print("3.")
print("a. =====")
print("D is 'all people'")
print("P is 'are blond'")
print("Q is 'are a westerner'")
print("Formal form: For all x in D, P(x) then Q(x)")

print('b. =====')
print("D is 'a person'")
print("P is 'hair is black'")
print("Q is 'a westerner'")

print('c. =====')
print("D is 'students'")
print("P is 'study correctly'")
print("Q is 'have high score'")

print('d. =====')
print("D is 'mammal'")
print("P is 'live in the sea'")
print("Q is 'either dolphins or whales'")

print('e. =====')
print("D is 'bird'")
print("P is 'don't have wings and can swim'")
print("Q is 'penguins'")

print('f. =====')
print("D is 'a bird'")
print("P is 'have wing'")
print("Q is 'can't fly'")


' ' ' Exercise04 ' ' '
print("4.")
def formalConvertPQ(S):
    temp = str(S).split(',')
    D = temp[0].strip()
    P = ''
    if search("For all", D):
        D = D.replace('For all','')
        P = ' '.join(temp[1].strip().split()[1:]).split('then')
        Q = ' '.join(P[1].strip().split()[1:])
        P = ' '.join(P[0].strip().split()[2:])
    if search("Exist", D):
        D = D.replace('Exist','')
        P = ' '.join(temp[1].strip().split()[1:]).split('then')
        Q = ' '.join(P[1].strip().split()[1:])
        P = ' '.join(P[0].strip().split()[2:])
    if search('For every', D):
        D = D.replace('For every','')
        P = ' '.join(temp[1].strip().split()[1:]).split('then')
        Q = ' '.join(P[1].strip().split()[1:])
        P = ' '.join(P[0].strip().split()[2:])
    return [D,P,Q]

' ' ' Exercise05 ' ' '
print("5.")
def nega(A):
    temp = formalConvert(str(A))
    D = temp[0]
    ans = ''
    if search('For all',str(A)):
        tempP = temp[1].split(' ')
        tempP[0] += ' not'
        P = ' '.join(tempP)
        ans = 'For all' + D + ', they ' + P
    return ans

print(nega('For all all fishes, they need water to survive'))










