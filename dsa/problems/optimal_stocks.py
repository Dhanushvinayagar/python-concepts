
def optimal_stocks(li):
    l=0
    current=0
    r=1

    # result
    res = 0 

    while r<len(li):
        if li[current]<li[r]:
            res = li[r]-li[l]
            current=r
        else:
            l=r
            current=l
        r+=1
    
    print(res)
    return res

# li=[4,3,2,1]
# li=[1,2,3,4]
li = [6,8,1,2,30,19]
optimal_stocks(li)