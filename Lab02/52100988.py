import itertools

' ' ' Exercise01 ' ' '
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

def Xor(p,q):
    return And(Or(p,q),Or(Not(p),Not(q)))

def Not(p):
    if p==True:
        return False
    else:
        return True
    
def Equipvalent(p,q):
    if p!=q:
        return False
    else:
        return True

' ' ' Exercise02 ' ' '
P = [True,True,False,False]
Q = [True,False,True,False]

def LImplies(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(Implies(p,q))
    return ans

def LAnd(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(And(p,q))
    return ans

def LOr(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(Or(p,q))
    return ans

def LXor(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(Xor(p,q))
    return ans

def LNot(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(Not(p,q))
    return ans

def LEquivalent(P,Q):
    ans = []
    for p,q in zip(P,Q):
        ans.append(Equipvalent(p,q))
    return ans

' ' ' Exercise03 ' ' '
# p ^ q -> r
table = list(itertools.product([False,True],repeat=2))
for i in table:
    for j in i:
        print(j,end=', ')
    print(And(i[0],i[1]))

# r -> p ^ q
for i in table:
    print(And(i[0],i[1]), ',', i[0], ',', i[1])

' ' ' Exercise04 ' ' '
# 
table = list(itertools.product([False,True],repeat=2))
print('p \t q \t r \t p v q -> p ^ q -> ~p v ~q')
for p,q in table:
    print(p,'\t',q,'\t',end='\t\t')
    temp = Or(p,q)
    temp = Implies(temp,And(p,q))
    temp = Implies(temp,Or(Not(p),Not(q)))
    print(temp)

# 
table = list(itertools.product([False,True],repeat=3))
print('p \t q \t r \t ~p v (q ^ r) -> r')
for p,q,r in table:
    print(p,'\t',q,'\t',r,end='\t\t')
    temp = Not(p)
    temp = Implies(temp,And(q,r))
    temp = Implies(temp,r)
    print(temp)

# 
print('p \t q \t r \t (p -> q) ^ (q -> r)')
for p,q,r in table:
    print(p,'\t',q,'\t',r,end='\t\t')
    temp = Implies(p,q)
    temp = And(temp,Implies(q,r))
    print(temp)

# 
print('p \t q \t r \t (p v (q ^ r)) <-> ((p v q) ^ (p v r))')
for p,q,r in table:
    print(p,'\t',q,'\t',r,end='\t\t')
    t1 = Or(p,And(q,r))
    t2 = And(Or(p,q),Or(p,r))
    temp = Equipvalent(t1,t2)
    print(temp)

# 
table = list(itertools.product([False,True],repeat=4))
print('p \t q \t r \t t \t p v q -> ~r v t')
for p,q,r,t in table:
    print(p,'\t',q,'\t',r,'\t',t,end='\t\t')
    t1 = Or(p,q)
    t2 = Or(Not(r),t)
    temp = Implies(t1,t2)
    print(temp)

# 
print('p \t q \t r \t t \t p v t -> q -> (r -> t)')
for p,q,r,t in table:
    print(p,'\t',q,'\t',r,'\t',t,end='\t\t')
    t1 = Or(p,t)
    temp = Implies(t1,q)
    t2 = Implies(r,t)
    temp = Implies(temp,t2)
    print(temp)

# 
print('p \t q \t r \t t \t (p v (q ^ r)) <-> ((p v q) ^ (p v r)) ^ (t v ~t))')
for p,q,r,t in table:
    print(p,'\t',q,'\t',r,'\t',t,end='\t\t')
    t1 = Or(p,And(q,r))
    t2 = And(And(Or(p,q),Or(p,r)),Or(t,Not(t)))
    temp = Implies(temp,t2)
    print(temp)

' ' ' Exercise05 ' ' '
# 
table = list(itertools.product([False,True],repeat=1))
count = 0
for p in table:
    if not Equipvalent(p,Not(Not(p))):
        print("Inequivalent")
        break
    else:
        count += 1
if count == len(table):
    print("equivalent")
# 
table = list(itertools.product([False,True],repeat=2))
count = 0
for p,q in table:
    count += 1
    if not Equipvalent(And(Not(Not(And(q,p))),(Or(q,p))),q):
        print("Inequivalent")
        break
    else:
        count += 1
if count == len(table):
    print("equivalent")

# 
count = 0
for p,q in table:
    count += 1
    if not Equipvalent(Not(Or(p,q)),(Or(Not(p),Not(q)))):
        print("Inequivalent")
        break
    else:
        count += 1
if count == len(table):
    print("equivalent")
# 
# 
# 
# 

' ' ' Exercise06 ' ' '
# so sánh tất cả các mệnh đề
table = list(itertools.product([False,True],repeat=4))





