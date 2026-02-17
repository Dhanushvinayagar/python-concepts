def lengthOfLongestSubstring_bf(s):

    s_length = 0

    n = len(s)

    for i in range(n):
        for j in range(i,n):
            s_set = set()
            for k in s[i:j+1]:
                if k in s_set:
                    break    
                s_set.add(k)
            else:
                s_length = max(s_length,j-i+1)

    print(s_length)

def lengthOfLongestSubstring(s):
    max_length = 0

    left = 0

    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        
    print(max_length)
    return max_length

s = "pwwkew"
# lengthOfLongestSubstring_bf(s)
lengthOfLongestSubstring(s)