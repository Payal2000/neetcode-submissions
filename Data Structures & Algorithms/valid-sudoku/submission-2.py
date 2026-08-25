class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range (9)]

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                box_radius = (r//3) * 3 + (c//3) 

                if val in rows[r]:
                    return False

                if val in cols[c]:
                    return False

                if val in box[box_radius]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                box[box_radius].add(val)


        return True

                





        



        