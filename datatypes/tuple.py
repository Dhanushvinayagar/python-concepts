t = (1,2,3,4,5)

print(t)
print(t[0])
print(t[-1])
     
try:
    t[0] = 10
except Exception as e: 
    print(e)

# add elements to tuple
t1 = t + (6,7)
print(t1)

# remove elements from tuple
t2 = t1[0:-1]
print(t2)   

# delete tuple  
del t

# empty tuple
t = ()
print(t)

# single element tuple
t = (1,)
print(t)

# tuple unpacking
t = (1,2,3,4,5)
a,b,c,d,e = t
print(a,b,c,d,e)

# tuple methods
print(t.count(1))
print(t.index(1))

# tuple to list
t = (1,2,3,4,5)
l = list(t)
print(l)

# list to tuple
l = [1,2,3,4,5]
t = tuple(l)
print(t)

# tuple to string
t = (1,2,3,4,5)
s = str(t)
print(s)

# string to tuple
s = "1,2,3,4,5"
t = tuple(s)
print(t)

# tuple to set
t = (1,2,3,4,5)
s = set(t)
print(s)

# set to tuple
s = {1,2,3,4,5}
t = tuple(s)
print(t)

# tuple to dictionary
t = (1,2,3,4,5)
d = dict.fromkeys(t)
print(d)

# dictionary to tuple
d = {1:"a",2:"b",3:"c",4:"d",5:"e"}
t = tuple(d)
print(t)

# tuple to frozenset
t = (1,2,3,4,5)
f = frozenset(t)
print(f)