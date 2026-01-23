
def find_missing_number(li):
    li_sum = 0 
    act_sum = 0
    for i in range(len(li)+1):
        act_sum += i

    for el in li:
        li_sum += el

    return act_sum - li_sum

# [0,n]
li = [3,0,4,2,1] 
print( find_missing_number(li) )