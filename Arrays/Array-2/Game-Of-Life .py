class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if board == []:
            return []
        
        # STATE CHANGES:
        # alive nbrs count: == 3       0 -> 1   ~ 3    
        # alive nbrs count: 2 or 3     1 -> 1
        # alive nbrs count: <2         1 -> 0   ~ 2    UNDER-POPULATION
        # alive nbrs count: > 3        1 -> 0   ~ 2    OVER-POPULATION
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                # COUNT # OF ACTIVE NBRS
                active_nbrs = 0
                cell_state = board[i][j] 
                for dir in dirs:
                    r = i+dir[0]
                    c = j+dir[1]
                    # Counting originally Active ngbrs --> 1 or 2
                    if 0 <= r <= len(board)-1 and 0 <= c <= len(board[0])-1:
                        if board[r][c] == 1 or board[r][c] == 2:
                            active_nbrs += 1
                
                if cell_state == 1:
                    # check if they ALIVE CELLS die due to UNDER-POPULATION or OVER-POPULATION
                    if active_nbrs < 2 or active_nbrs > 3:  
                        board[i][j] = 2         # 2 in the board indicates 1->0
                    
                elif cell_state == 0 and active_nbrs == 3:
                    # check if DEAD CELLS can become alive
                    board[i][j] = 3             # 3 in the board indicates 0->1
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
                    
        return board
                    
                
                    
                        