class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rowSearch(matrix):
            l, r = 0, len(matrix) - 1
            while l <= r:
                m = l + (r - l) // 2
                if matrix[m] == target:
                    return True
                elif matrix[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        l_row, r_row = 0, len(matrix) - 1

        while l_row <= r_row:
            m = l_row + (r_row - l_row) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return rowSearch(matrix[m])
            elif matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l_row = m + 1
            else:
                r_row = m - 1

        return False

        