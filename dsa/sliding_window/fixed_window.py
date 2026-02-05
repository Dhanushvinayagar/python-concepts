# fixed sliding window
 
def greatest_k_sum(li,k):
    
    max_sum = 0

    for i in range(0,k):
        max_sum+=li[i]

    window_sum = max_sum
    for i in range(k,len(li)):
        window_sum = window_sum + li[i] - li[i-k]
        if window_sum > max_sum:
            max_sum=window_sum

    print(max_sum)
    return

li = [1,2,9,3,4,5]
k=3
greatest_k_sum(li,k)