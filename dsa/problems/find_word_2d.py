# recursive backtracking 
def find_word_paths(board, word):
    r = len(board)
    c = len(board[0])
    word_len = len(word)

    def dfs(row,col,word_index,visited):
        if word_len <=word_index:
            print("Match found")
            return True
        
        if row<0 or col <0 or row>=r or col>=c:
            return False

        if (row,col) in visited:
            return False
        else:
            visited.append((row,col))

        if li[row][col] == word[word_index]:
            return dfs(
                row+1,col,word_index+1,visited
            ) or dfs(
                row-1,col,word_index+1,visited
            ) or dfs(
                row,col+1,word_index+1,visited
            ) or dfs(
                row,col-1,word_index+1,visited
            )

        return False

    for row in range(r):
        for col in range(c):
            if dfs(row,col,0,[]):
                return True
    
    return False



word = "ABBCDE"
li = [
    ["E","B","C","D"],
    ["B","B","C","E"],
    ["A","A","D","E"],
    ["M","N","O","P"]
]


# word="BD"
# li= [
#     ["A","B"],
#     ["C","D"]
# ]
res = find_word_paths(li,word)
print(res)