def repeatedcharpattern(sen):
    res = ""
    l=0
    r=1

    n = len(sen)
    for _ in range(n):
        if r==n:
            res += sen[l] + str(n-l)
        elif sen[l]==sen[r]:
            r+=1
        else:
            res += sen[l] + str(r-l)
            l=r
            r+=1
    return res

s = "abbbcddeefff"
print(repeatedcharpattern(s))