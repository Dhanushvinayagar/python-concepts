# works only for sorted list
def binary_search(li,key):

    start = 0
    end = len(li)-1

    while start<=end:
        mid = start + (end-start)//2
       
        if li[mid]==key:
            return str(key) + " found in list"
        elif li[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

        print(start,end,mid)
    return str(key) + " not found"

li = [1,2,3,4,5,6,7,9]
element = 2
res = binary_search(li,element)
print(res)