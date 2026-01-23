
res = lambda x,y:x+y
s = res(10,20)
print(s)

def squareFn(n):
    return n*n

li=[1,2,3,4,5]
squared = list(map(squareFn,li))
print(squared)


def filterFn(x):
    return x%2==0

li=[1,2,3,4,5]
odd = list(filter(filterFn,li))
print(odd)