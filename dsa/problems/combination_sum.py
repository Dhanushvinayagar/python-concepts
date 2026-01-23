
def combination(li):
    res = []
    res.append([])

    for i in range(0,len(li)):
        res.append([li[i]])
        l = [li[i]]
        for j in range(i+1,len(li)):
            l.append(li[j])
            res.append(l)
            l=l[:]
    return res

li = [1,2,3]
combination(li)