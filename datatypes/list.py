from random import randint


li=[]

for i in range(5):
    num = randint(1,100)
    li.append(num)

print(li)

li.sort()
print(li)

li.sort(reverse=True)
print(li)

li.reverse()
print(li)

li.insert(2,50)
print(li)

li.remove(50)
print(li)

li.pop()
print(li)

li.pop(1)
print(li)   


li.remove(li[1])
print(li)

print(li.count(li[1]))

print(li.index(li[1]))

li2=[1,2,3,4,5]
li.extend(li2)
print(li)   

li3=li.copy()
print(li3)  

l = li + li2
print(l)

li.clear()
print(li)

li = list(set(li))
print(li)

li = list(dict.fromkeys(li))
print(li)

li = [1,2,3,4,5]
li = [x*2 for x in li]
print(li)

li = [*li]
print(li)

li = list(map(lambda x:x*2,li))
print(list(li))


print(li[::-1])
print(li[0:3])
print(li[-5:2])