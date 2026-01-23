
def linear_search(li,key):

    for el in li:
        if el == key:
            return str(el) + " found in list"
    return str(el) + " not found"

li = [1,23,4,2,25]
element = 10
res = linear_search(li,element)
print(res)