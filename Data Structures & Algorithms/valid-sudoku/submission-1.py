class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = {0: {all numbers of 0th row}, 1: {}, 2: {}, 3: ...}
        rows = defaultdict(set)
        # cols = {0: {all element of 0th col}, 1: {}, 2: {}, 3: ...}
        cols = defaultdict(set)
        # squares = {(0, 0): {}, (0, 1): {}, (0, 2): {}, 
        #           (1, 0): {}, (1, 1): {}, (1, 2): {},
        #           (2, 0): {}, (2, 1): {}, (2, 2): {}
        #             }
        squares = defaultdict(set)


        for c in range(len(board)):
            for r in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
