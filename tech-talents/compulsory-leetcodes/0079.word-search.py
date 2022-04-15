#!/usr/bin/python3

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        result = False
        for row in range(len(board)):
        	for col in range(len(board[0])):
        		if self.dfs(board, word, row, col, 0):
        			return True
        return False

    def dfs(self, board, word, row, col, curr_len):
    	if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
    		return False
    	if board[row][col] == word[curr_len]:
    		c = board[row][col]
    		board[row][col] = '#'

    		if curr_len == len(word) - 1:
    			return True
    		elif (self.dfs(board, word, row-1, col, curr_len+1) or self.dfs(board, word, row+1, col, curr_len+1) or self.dfs(board, word, row, col-1, curr_len+1) or self.dfs(board, word, row, col+1, curr_len+1)):
    			return True

    		board[row][col] = c
    	return False

# UNIT TESTING #
pino = Solution()

# EXAMPLE 1
#
# board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED" 
#
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"
print(pino.exist(board,word))

# EXAMPLE 2
#
# board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE"
#
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="SEE"
print(pino.exist(board,word))

# EXAMPLE 3
#
# board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB"
#
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCB"
print(pino.exist(board,word))
