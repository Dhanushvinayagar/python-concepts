s = set()   

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

s.add(2)
s.add(3)
s.add(4)

print(s)

s.remove(4)
print(s)

s.discard(4)
print(s)

s.clear()
print(s)

print(len(s))

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

print(s | s1)
print(s & s1)
print(s - s1)   
print(s ^ s1)

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

print(s <= s1)
print(s >= s1)
print(s < s1)
print(s > s1)

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

s.update(s1)
print(s)

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

s.intersection_update(s1)
print(s)

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

s.difference_update(s1)
print(s)

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}

s.symmetric_difference_update(s1)
print(s)

