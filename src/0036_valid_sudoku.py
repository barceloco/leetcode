class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(r):
            seen = set()
            for i in range(len(board)):
                el = board[r][i]
                if el in seen:
                    return False
                if not el == ".":
                    seen.add(el)
            return True
        def check_column(c):
            seen = set()
            for i in range(len(board)):
                el = board[i][c]
                if el in seen:
                    return False
                if not el==".":
                    seen.add(el)
            return True
        def check_box(b):
            seen = set()
            br = 3*(b%3)
            bc = 3*(b//3)
            for i in range(len(board)):
                el = board[br+i%3][bc+i//3]
                if el in seen:
                    return False
                if not el == ".":
                    seen.add(el)
            return True
        valid = True
        for i in range(9):
            valid = valid and check_row(i)
            valid = valid and check_column(i)
            valid = valid and check_box(i)
        return valid