input = "abc"

def combinations(combo):
    print(combo)
    if(len(combo)==len(input)):
        return
    for c in input:
        if c not in combo:
            combinations(combo+c)


for letter in input:
    combinations(letter)
