 class Chess: 
    def __init__(self, board):
        self.board = board.split() #board_array

    #check the board 
    def check_board(self, board):
        #the board has to remain square
        ##check if element of board_array is equal len of board
        for row in self.board:
        ##row is the element in the board_array
            if (len(row) != len(self.board)):
                return False
        ##check if there is one King
        if board.count("K") != 1 #K is the keyword 
            return False
        ##check the chess pieces n invalid pieces
        ###remove the duplicates in str_b_list
        b_set = set("".join(self.board))
        for p in b_set:
            if p not in ["P", "B", "R", "Q", "."]: #not in operator
            return False
        return True
    
    #find the king position
    #using the loop
    
    
