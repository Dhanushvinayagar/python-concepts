def pair_sum_m1(li,target):
    n = len(li)
    # method 1 
    for i in range(n):
        for j in range(i+1,n):
            if target == li[i] + li[j]:
                print(i,j)
                return [i,j]
    return []

def pair_sum_m2(li,target):
    n = len(li)
    hm = {}
    for i in range(n):
        if hm.get(li[i],None) is not None:
            return [hm.get(li[i]),li[i]]

        hm[target-li[i] if target > li[i] else li[i]-target] = li[i] 

    return []

li=[4,9,2,1,7]
target = 5
pair_sum_m1(li,target)
pair_sum_m2(li,target)