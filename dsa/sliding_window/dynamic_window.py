# dynamic sliding window

def target_sum_length(li,target):
    l = 0
    r = 1

    while l<r and l<len(li):
    
        s = li[l]
        t = l+1
        while t<len(li) and s < target:
            s+=li[t]
            if t>r:
                r+=1
            t+=1
        print(l,r, "Sum : ",s , " with range : ", r-l+1)
        l+=1


    return

li = [2,3,1,2,1,4,3,0]

target = 7
target_sum_length(li,target)
