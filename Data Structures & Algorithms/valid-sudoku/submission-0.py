class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue
                
                box_keys = (i // 3, j // 3)
                
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[box_keys]:
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[box_keys].add(board[i][j])

        return True

                # if board[i][j] in rows[i]:
                #     return False
                # rows[i].add(board[i][j])

                # if board[i][j] in columns[j]:
                #     return False
                # columns[j].add(board[i][j])

                # if board[i][j] in boxes[box_keys]:
                #     return False
                # boxes[box_keys].add(board[i][j])
        # return True
        

