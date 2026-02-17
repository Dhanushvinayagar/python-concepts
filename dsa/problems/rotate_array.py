
def rotate_array_bf():
    li = [1,2,3,4,5,6,7]

    k=3

    for i in range(k):
        temp = li[-1]
        for j in range(len(li)-1,0,-1):
            li[j] = li[j-1]
        li[0] = temp

    print(li)
    return

def rotate_array():
    li = [1,2,3,4,5,6,7]

    k=3

    n=len(li)
    def reverse(start,last):
        while start<last:
            li[start], li[last] = li[last], li[start]
            start+=1
            last-=1
        return

    # reverse whole list
    reverse(0,n-1)
    # rotate till k
    reverse(0,k-1)
    # rotate from k
    reverse(k,n-1)

    print(li)
    
    return

rotate_array()
