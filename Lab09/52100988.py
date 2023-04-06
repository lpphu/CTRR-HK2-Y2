# 52100988 Lữ Phúc Phú

import string
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

''' Example '''

''' Exercise 01 '''
# a.
def mPus(A,B):
    ans = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            temp.append(A[i][j]+B[i][j])
        ans.append(temp)
    return np.array(ans)

# b.
def mMinus(A,B):
    ans = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            temp.append(A[i][j]-B[i][j])
        ans.append(temp)
    return np.array(ans)

# c.
def mMultiply(A,B):
    ans = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A)):
            t = 0
            for k in range(len(A)):
                t += A[i][k]*B[k][j]
            temp.append(t)
        ans.append(temp)
    return np.array(ans)

''' Exercise 02 '''
A = np.array([[0,0,3,0,1],
              [0,0,5,3,0],
              [3,5,0,1,0],
              [0,3,1,0,2],
              [1,0,0,2,0]])
def ex02a(A):
    G1 = nx.from_numpy_array(A, create_using=nx.DiGraph)
    pos=nx.spring_layout(G1)
    nx.draw_networkx(G1,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcde')})
    edge_labels = nx.draw_networkx_edge_labels(G1,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show() 

B = np.array([[0,0,0,0,1,1],
              [0,0,5,3,0,0],
              [0,5,0,1,5,0],
              [0,3,1,0,2,3],
              [1,0,5,2,0,6],
              [1,0,0,3,6,0]])
def ex02b(B):
    G1 = nx.from_numpy_array(B, create_using=nx.DiGraph)
    pos=nx.spring_layout(G1)
    nx.draw_networkx(G1,pos=pos,with_labels=True,labels={a:b for
    a,b in enumerate('abcdef')})
    edge_labels = nx.draw_networkx_edge_labels(G1,font_size=6,
    pos=pos,label_pos=0.5)
    plt.axis('equal')
    plt.show() 

''' Exercise 03 '''
A = [('A','B',5),
         ('A','D',3), 
         ('B','C',3), 
         ('B','D',2), 
         ('C','D',1),
         ('C','E',3),
         ('D','E',1),
         ('D','F',3),
         ('E','F',4)]

def ex03a(A):
    G = nx.Graph()
    G.add_weighted_edges_from(A)

    pos=nx.spring_layout(G)
    w = nx.adjacency_matrix(G, weight='weight').todense()
    nx.draw_networkx(G, pos=pos, with_labels=True)
    edge_labels = nx.draw_networkx_edge_labels(G, font_size=6, pos=pos, label_pos=0.5)
    plt.axis('equal')
    plt.show()

B = [('A','C',2),
     ('A','D',3), 
     ('A','E',3), 
     ('B','C',3), 
     ('B','D',2),
     ('C','D',2),
     ('C','E',8),
     ('C','F',6),
     ('D','F',5),
     ('E','F',3)]

def ex03b(B):
    G = nx.Graph()
    G.add_weighted_edges_from(B)

    pos=nx.spring_layout(G)
    w = nx.adjacency_matrix(G, weight='weight').todense()
    nx.draw_networkx(G, pos=pos, with_labels=True)
    edge_labels = nx.draw_networkx_edge_labels(G, font_size=6, pos=pos, label_pos=0.5)
    plt.axis('equal')
    plt.show()

''' Exercise 04 '''
def toLoE(A):
    res= []
    chars = list(string.ascii_uppercase)
    my_dict = {i: chars[i] for i in range(len(A))}
    for i in range(len(A)):
        it = []
        for j in range(len(A[0])):
            if( i != j ):
                it.append( (my_dict[i], my_dict[j], A[i][j]  ));
        res.append(it)
    return res

print(toLoE(A))