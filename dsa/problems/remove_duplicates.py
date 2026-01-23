# sorted array
li = [1,1,1,2,3,3,4,4,4,4,5,6,6,6,6,6,7,7,8,8,9,9]

# method 1
res = []
for i in li:
    if i not in res:
        res.append(i)

# method 2
hm= {}
for i in li:
    hm[i]=True

for i in li:
    if hm[i]:
        print(i)
        hm[i]=False

# method 3
l=0
r=1

length = len(li)
for i in range(length):
    if r<length and li[l]==li[r]:
        r+=1
    elif r<length:
        l+=1
        li[l] = li[r]
        r+=1

print(li[:l+1])