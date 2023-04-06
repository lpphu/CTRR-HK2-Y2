# 52100988 Lữ Phúc Phú

''' Exercise 01 '''
Andersen = set(["The Emperor's New Clothes","The Little Mermaid","The Little Match Girl","The Snow Queen"])

''' Exercise 02 '''
Shakespeare = set(["Romeo and Juliet","Hamlet","King Lear","Macbeth","A Midsummer Night's Dream","A Comedy of Errors"])

''' Exercise 03 '''
Tragedy = set(["Medea", "Octavia", "Oedipus", "Ur-Hamlet"])
Comedy = set(["The Three Musketeer", "The Clouds"])
Uncategory = set(["Don Quixote", "Rapunzel", "Cinderella"])

''' Exercise 04 '''
Shakespeare_Tragedy = Shakespeare.difference(Tragedy)

''' Exercise 05 '''
Andersen_Comedy = Andersen.intersection(Comedy)

''' Exercise 06 '''
print("Andersen_Comedy have relationship with Shakespeare issubset:" , Andersen_Comedy.issubset(Shakespeare))
print("Andersen_Comedy have relationship with Shakespeare issuperset:" , Andersen_Comedy.issuperset(Shakespeare))
print("Andersen_Comedy have relationship with Shakespeare isdisjoint:" , Andersen_Comedy.isdisjoint(Shakespeare))

print("Andersen_Comedy have relationship with Andersen issubset:" , Andersen_Comedy.issubset(Andersen))
print("Andersen_Comedy have relationship with Andersen issuperset:" , Andersen_Comedy.issuperset(Andersen))
print("Andersen_Comedy have relationship with Andersen isdisjoint:" , Andersen_Comedy.isdisjoint(Andersen))

print("Andersen_Comedy have relationship with Tragedy issubset:" , Andersen_Comedy.issubset(Tragedy))
print("Andersen_Comedy have relationship with Tragedy issuperset:" , Andersen_Comedy.issuperset(Tragedy))
print("Andersen_Comedy have relationship with Tragedy isdisjoint:" , Andersen_Comedy.isdisjoint(Tragedy))

print("Andersen_Comedy have relationship with Comedy issubset:" , Andersen_Comedy.issubset(Comedy))
print("Andersen_Comedy have relationship with Comedy issuperset:" , Andersen_Comedy.issuperset(Comedy))
print("Andersen_Comedy have relationship with Comedy isdisjoint:" , Andersen_Comedy.isdisjoint(Comedy))

print("Andersen_Comedy have relationship with Uncategory issubset:" , Andersen_Comedy.issubset(Uncategory))
print("Andersen_Comedy have relationship with Uncategory issuperset:" , Andersen_Comedy.issuperset(Uncategory))
print("Andersen_Comedy have relationship with Uncategory isdisjoint:" , Andersen_Comedy.isdisjoint(Uncategory))

print("Shakespeare_Tragedy have relationship with Shakespeare issubset:" , Shakespeare_Tragedy.issubset(Shakespeare))
print("Shakespeare_Tragedy have relationship with Shakespeare issuperset:", Shakespeare_Tragedy.issuperset(Shakespeare))
print("Shakespeare_Tragedy have relationship with Shakespeare isdisjoint:" , Shakespeare_Tragedy.isdisjoint(Shakespeare))

print("Shakespeare_Tragedy have relationship with Andersen issubset:" , Shakespeare_Tragedy.issubset(Andersen))
print("Shakespeare_Tragedy have relationship with Andersen issuperset:" , Shakespeare_Tragedy.issuperset(Andersen))
print("Shakespeare_Tragedy have relationship with Andersen isdisjoint:" , Shakespeare_Tragedy.isdisjoint(Andersen))

print("Shakespeare_Tragedy have relationship with Tragedy issubset:" , Shakespeare_Tragedy.issubset(Tragedy))
print("Shakespeare_Tragedy have relationship with Tragedy issuperset:" , Shakespeare_Tragedy.issuperset(Tragedy))
print("Shakespeare_Tragedy have relationship with Tragedy isdisjoint:" , Shakespeare_Tragedy.isdisjoint(Tragedy))

print("Shakespeare_Tragedy have relationship with Comedy issubset:" , Shakespeare_Tragedy.issubset(Comedy))
print("Shakespeare_Tragedy have relationship with Comedy issuperset:" , Shakespeare_Tragedy.issuperset(Comedy))
print("Shakespeare_Tragedy have relationship with Comedy isdisjoint:" , Shakespeare_Tragedy.isdisjoint(Comedy))

print("Shakespeare_Tragedy have relationship with Uncategory issubset:" , Shakespeare_Tragedy.issubset(Uncategory))
print("Shakespeare_Tragedy have relationship with Uncategory issuperset:" , Shakespeare_Tragedy.issuperset(Uncategory))
print("Shakespeare_Tragedy have relationship with Uncategory isdisjoint:" , Shakespeare_Tragedy.isdisjoint(Uncategory))

''' Exercise 07 '''
Work = Andersen.union(Shakespeare).union(Comedy).union(Tragedy).union(Uncategory)

''' Exercise 08 '''
Author = set(["Andersen","Shakespeare","Unknown"])

''' Exercise 09 '''
Author_Of = dict()
for i in Work:
    if i in Andersen:
        Author_Of[i] = "Andersen"
    if i in Shakespeare:
        Author_Of[i] = "Shakespeare"
    else:
        Author_Of[i] = "Unknow"
print(Author_Of['Medea'])

''' Exercise 10 '''
Writen_By = dict()
Writen_By["Andersen"] = Andersen
Writen_By["Shakespeare"] = Shakespeare
Writen_By["Unknown"] = Work.difference(Andersen).difference(Shakespeare)

''' Exercise 11 '''
Work_Count = dict()
Work_Count["Andersen"] = Andersen.__len__
Work_Count["Shakespeare"] = Shakespeare.__len__
Work_Count["Unknown"] = Work.difference(Andersen).difference(Shakespeare).__len__

''' Exercise 12 '''
num_word = len("In the span of humanity, writing are what enabled humans to pass on many knowledge to their next generation. Via writing, the art of telling stories; both fictional and real; evolved and became a huge part of humanity culture. Among them, there are stories that transcend languages, culture and history to reach people far away both in spaces and times. Some prominent examples are the works of Shakespeare, Andersen, Homer,...")

''' Exercise 13 '''



