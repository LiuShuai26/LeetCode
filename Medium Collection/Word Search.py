class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        book = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    book[i][j] = 1
                    if self.helper(i, j, 1, board, word, book):
                        return True
                    book[i][j] = 0
        return False

    def helper(self, m, n, k, board, word, book):
        if k == len(word):
            return True
        if m-1 >= 0 and word[k] == board[m-1][n] and book[m-1][n] == 0:
            book[m-1][n] = 1
            res = self.helper(m-1, n, k+1, board, word, book)
            if res:
                return res
            book[m-1][n] = 0
        if m+1 < len(board) and word[k] == board[m+1][n] and book[m+1][n] == 0:
            book[m+1][n] = 1
            res = self.helper(m+1, n, k+1, board, word, book)
            if res:
                return res
            book[m+1][n] = 0
        if n-1 >= 0 and word[k] == board[m][n-1] and book[m][n-1] == 0:
            book[m][n-1] = 1
            res = self.helper(m, n-1, k+1, board, word, book)
            if res:
                return res
            book[m][n-1] = 0
        if n+1 < len(board[0]) and word[k] == board[m][n+1] and book[m][n+1] == 0:
            book[m][n+1] = 1
            res = self.helper(m, n+1, k+1, board, word, book)
            if res:
                return res
            book[m][n+1] = 0


s = Solution()
print(s.exist(
[["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB"))
