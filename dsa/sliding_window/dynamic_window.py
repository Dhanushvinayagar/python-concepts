# dynamic sliding window

def target_sum_length(li,target):
    l = 0
    window_sum = 0
    result = len(li)

    for r in range(len(li)):
        window_sum += li[r]          # expand

        while window_sum >= target:  
            result = min(result, r - l + 1)  
            window_sum -= li[l]      # shrink
            l += 1

    print(result)
    return  

li = [2,3,1,2,1,4,3,0]

target = 7
target_sum_length(li,target)
