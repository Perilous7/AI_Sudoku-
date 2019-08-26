
# coding: utf-8

# In[ ]:



import copy, time
import random, math

domain_dict = {}



def getEasyBoards():
    easy_1 = [
        [5,0,2,9,4,3,8,0,0],
        [3,0,8,2,6,0,0,7,5],
        [0,0,4,0,0,0,0,2,0],
        [2,0,0,8,5,9,6,0,7],
        [0,6,0,0,0,0,0,0,8],
        [0,4,9,6,0,2,5,0,1],
        [9,0,0,0,1,0,3,0,0],
        [0,8,0,7,0,0,0,5,0],
        [1,0,0,0,0,5,7,0,0]
    ]
    easy_2 = [
        [6,0,8,9,0,0,7,0,0],
        [4,0,0,8,6,0,9,0,0],
        [3,0,0,0,7,0,6,0,8],
        [9,0,3,0,2,0,4,0,0],
        [0,0,4,0,5,7,0,0,3],
        [0,0,0,4,0,9,8,5,0],
        [8,9,0,0,4,5,0,0,0],
        [5,0,0,2,0,0,3,0,9],
        [0,0,6,7,0,1,0,0,4]
    ]
    easy_3 = [
        [0,3,1,8,0,7,4,0,6],
        [0,0,9,0,0,1,0,7,3],
        [0,0,0,0,0,0,0,0,8],
        [0,5,0,9,0,8,0,1,0],
        [0,7,4,3,2,0,0,6,9],
        [0,0,0,4,0,0,0,0,0],
        [0,2,3,0,8,4,0,5,0],
        [0,6,8,0,0,3,9,4,0],
        [0,1,5,7,0,0,0,0,2]
    ]
    easy_4 = [
        [0,0,3,0,0,6,5,0,0],
        [0,5,0,2,0,8,0,6,0],
        [6,0,0,0,4,5,0,0,3],
        [0,0,0,6,7,0,2,5,1],
        [0,0,2,8,0,1,0,0,4],
        [5,1,0,9,0,0,8,0,0],
        [2,4,5,3,8,0,0,0,0],
        [0,0,1,0,6,0,0,8,5],
        [0,9,0,0,1,7,4,0,0]
    ]
    easy_5 = [
        [5,0,9,0,0,4,0,0,3],
        [7,6,0,5,0,3,0,8,9],
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,2,0,0,0,4,8],
        [4,0,7,9,0,6,1,5,0],
        [0,0,0,0,0,0,0,6,0],
        [1,0,0,3,0,2,0,9,0],
        [0,4,6,7,0,8,0,0,5],
        [0,0,2,1,0,5,8,0,6]
    ]

    return easy_1, easy_2, easy_3, easy_4, easy_5

def getMediumBoards():

    medium_1 = [
        [7,8,0,0,0,0,0,5,0],
        [0,0,0,1,0,0,0,0,0],
        [9,0,0,0,6,0,7,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,6,8,0,0,0,0,1],
        [0,5,0,0,0,0,0,9,4],
        [0,0,1,7,2,0,9,0,0],
        [0,0,0,0,8,0,2,7,0],
        [0,7,5,9,0,0,0,0,0]
    ]
    medium_2 = [
        [0,3,0,9,0,6,0,0,0],
        [0,0,0,8,5,0,0,2,9],
        [0,7,0,0,0,0,4,0,6],
        [4,0,5,0,0,0,8,0,0],
        [0,0,0,0,9,0,0,0,0],
        [0,0,0,0,0,8,0,3,2],
        [0,0,0,0,0,0,0,5,0],
        [1,0,7,0,0,4,0,0,0],
        [0,0,0,1,3,0,9,0,0]
    ]
    medium_3 = [
        [0,2,0,0,0,6,0,3,0],
        [0,0,0,0,0,0,2,0,0],
        [1,7,0,9,0,0,0,0,0],
        [5,0,4,0,0,0,3,0,0],
        [0,0,0,5,0,9,0,1,0],
        [0,0,1,0,0,2,4,5,0],
        [0,0,0,0,0,0,0,2,0],
        [9,0,0,3,5,0,0,0,0],
        [0,0,5,0,1,0,6,0,0]
    ]
    medium_4 = [
        [0,0,0,7,0,0,0,0,0],
        [0,2,8,0,0,0,0,0,3],
        [0,0,0,5,0,8,0,6,1],
        [0,0,5,0,2,6,0,0,9],
        [0,0,0,0,0,0,0,0,0],
        [0,3,0,0,9,0,5,0,4],
        [0,0,0,0,0,0,0,4,0],
        [0,0,0,4,5,0,6,1,0],
        [0,4,6,0,8,0,0,0,0]
    ]
    medium_5 = [
        [0,1,0,0,5,0,9,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,7,8,0,0,0,4,0,0],
        [0,0,0,0,0,0,0,0,0],
        [1,9,2,0,0,6,0,1,0],
        [3,0,0,0,0,6,0,1,0],
        [0,0,0,8,0,0,0,0,7],
        [0,6,0,7,0,0,0,5,0],
        [8,0,0,3,1,0,0,0,2]
    ]
    return medium_1, medium_2, medium_3, medium_4, medium_5

def getHardBoards():


    hard_1 = [
        [0,0,0,2,0,5,0,0,0],
        [0,1,0,0,0,0,0,0,8],
        [0,0,0,4,0,3,0,0,0],
        [0,0,1,8,0,0,0,0,0],
        [3,6,0,0,0,0,0,0,0],
        [0,5,0,0,9,4,2,0,0],
        [0,0,0,0,0,2,0,4,0],
        [0,0,0,0,0,0,6,0,7],
        [8,0,0,3,7,0,0,0,1]
    ]
    hard_2 = [
        [0,5,0,0,0,0,4,0,0],
        [0,0,7,0,0,5,0,0,0],
        [0,0,0,3,0,0,0,2,0],
        [1,0,6,0,0,0,0,0,5],
        [0,0,0,0,0,7,1,0,3],
        [0,0,0,6,0,0,0,8,0],
        [5,2,0,0,1,0,0,0,0],
        [0,0,0,0,9,4,3,0,0],
        [0,0,9,7,0,0,0,4,0]
    ]
    hard_3 = [
        [0,2,5,0,0,0,0,0,0],
        [0,0,0,0,9,8,0,0,0],
        [0,0,0,0,0,0,7,5,0],
        [3,5,0,0,7,6,0,0,0],
        [1,0,8,0,0,0,0,0,0],
        [0,0,0,0,8,0,1,0,9],
        [8,1,0,0,0,7,0,0,0],
        [0,0,0,0,0,0,0,1,3],
        [0,0,0,0,1,3,9,0,6]
    ]
    hard_4 = [
        [0,0,0,6,0,0,0,0,7],
        [0,0,3,0,1,0,0,0,0],
        [0,7,0,0,0,0,2,0,0],
        [0,2,0,4,0,3,0,0,0],
        [0,0,8,0,5,0,0,0,0],
        [0,0,0,0,0,7,8,4,0],
        [9,6,0,3,0,0,0,0,0],
        [4,0,0,0,0,0,0,7,1],
        [0,0,2,0,6,0,9,0,0]
    ]
    hard_5 = [

    ]
    return hard_1, hard_2, hard_3, hard_4, hard_5


class State():
    def __init__(self, board, parent, move):
        self.board = board
        self.parent = parent
      

    def genBoard(self):
        for i in range(0, 9):
            print(self.board[i])
    def getCol(self, col_num):
        col = []
        for row in self.board:
            col.append(row[col_num])
        return col

    def getBlock(self, row_num, col_num):
        board = []

        for i in range(9):
            save = False
            block = []
            for j in range(9):
                if (i == row_num and j == col_num):
                    save = True
                block.append(self.board[i][j])
            if (save):
                board.extend(block)
                break
            block = []
        
        return board

    
    
    def onlyValidRows(self):
        valid = True
        for row in self.board:
            row = [x for x in row if x != 0]
            if (len(row) > 0):
                if (len(list(set(row))) < len(row)):
                    valid = False
                    break
                elif(max(row) > 9 or min(row) < 0):
                    valid = False
                    break
        return valid

    def numValidRows(self):
        valid = 0
        for row in self.board:
            row = [x for x in row if x != 0]
            if (len(row) > 0):
                if (len(list(set(row))) < len(row)):
                    continue
                elif(max(row) > 9 or min(row) < 0):
                    continue
                else:
                    valid += 1
        return valid

    def onlyValidCols(self):
        valid = True
        for i in range(0,9):
            col = []
            for row in self.board:
                col.append(row[i])
            col = [x for x in col if x != 0]
            if (len(col) > 0):
                if (len(list(set(col))) < len(col)):
                    valid = False
                    break
                elif (max(col) > 9 or min(col) < 0):
                    valid = False
                    break
        return valid


    def numValidCols(self):
        valid = 9
        for i in range(0,9):
            col = []
            for row in self.board:
                col.append(row[i])
            col = [x for x in col if x != 0]
            if (len(col) > 0):
                if (len(list(set(col))) < len(col)):
                    continue
                elif (max(col) > 9 or min(col) < 0):
                    continue
                else:
                    valid += 1
        return valid

    def onlyValidBlocks(self):
        valid = True
        board = []

        for i in range(9):
            block = []
            for j in range(9):
                block.append(self.board[i][j])
            board.append(block)
            block = []
        
        for block in board:
            block = [x for x in block if x != 0]
            if (len(block) > 0):
                if (len(list(set(block))) < len(block)):
                    valid = False
                    break
                elif(max(block) > 9 or min(block) < 0):
                    valid = False
                    break
        return valid

    def numValidBlocks(self):
        valid = 0
        board = []

        for i in range(9):
            block = []
            for j in range(9):
                block.append(self.board[i][j])
            board.append(block)
            block = []
        
        for block in board:
            block = [x for x in block if x != 0]
            if (len(block) > 0):
                if (len(list(set(block))) < len(block)):
                    continue
                elif(max(block) > 9 or min(block) < 0):
                    continue
                else:
                    valid += 1
        return valid

class BackTrack():
    def __init__(self):
        self.banned_moves = []

    def _accept(self, state):
        validBlocks = state.onlyValidBlocks()
        validCols = state.onlyValidCols()
        validRows = state.onlyValidRows()
        accepted = validBlocks and validCols and validRows
        return accepted

    def _solution(self, state):
        no_more_moves = True
        for row in state.board:
            if (0 in row):
                no_more_moves = False
                break
        return no_more_moves

    def _copy_board(self, board):
        copy_of_board = []
        for row in board:
            new_row = []
            for element in row:
                new_row.append(copy.deepcopy(element))
            copy_of_board.append(new_row)
        return copy_of_board

    def _getFirstEmpty(self, state):
        for row in range(len(state.board)):
            for col in range(len(state.board)):
                if (state.board[row][col] == 0):
                    return row,col

        return False


    def _next_ac3(self, state, sibling_moves):
        coords = self._getFirstEmpty(state)
        if (coords is not False):
            row_num= coords[0]
            col_num= coords[1]
            potential_moves = domain_dict[(row_num,col_num)]         
            for move in potential_moves:
                check = str(row_num)+":"+str(col_num)+":"+str(move)
                if (check not in sibling_moves):
                    sibling_moves.append(check)
                    state.board[row_num][col_num] = move
                    if (self._accept(state)):
                        return True
                    state.board[row_num][col_num] = 0
        return False

    def backtrack(self, state):
        if (self._solution(state) and self._accept(state)):
            return True
        sibling_moves = []
        move = self._next_ac3(state, sibling_moves)
        while(move):
            if (self._accept(state) and self.backtrack(state)):
                return True
            reverse_move = sibling_moves[-1].split(":")
            state.board[int(reverse_move[0])][int(reverse_move[1])] = 0
            move = self._next_ac3(state, sibling_moves)   

    def _possible_moves(self, state, row_num, col_num):
        col_moves = [x for x in range(1,10) if x not in state.getCol(col_num)]
        row_moves = [x for x in range(1,10) if x not in state.board[row_num]]
        block_moves = [x for x in range(1,10) if x not in state.getBlock(row_num, col_num)]
        return list(set(list(set(col_moves).intersection(row_moves))).intersection(block_moves))




    def _get_empty_cells(self, state):
        empty_cells = []
        for row_num in range(0,9):
            for col_num in range(0,9):
                if (state.board[row_num][col_num]==0):
                    empty_cells.append((row_num, col_num))
        return empty_cells
    
    def AC3(self, state):
        
        empty_cell_array = self._get_empty_cells(state)
        arc = []
        for cell in empty_cell_array:
            row = cell[0]
            col = cell[1]
            empty_neighbor = [x for x in list(set(self._gen_arcs(row, col)).intersection(empty_cell_array)) if x!=cell]
            for val in empty_neighbor:
                if val!=cell:
                    arc.append((cell,val))
           
        for empty in empty_cell_array:
            domain_dict[empty] = self._possible_moves(state,empty[0],empty[1])
    
    
        while(len(arc)>0):
            temp_arc = arc.pop(0)
            x_i=temp_arc[0]
            x_j=temp_arc[1]
            if (self.remove_inconsistancy_value(x_i,x_j)):
                if((len(domain_dict[x_i])==0) or (len(domain_dict[x_j])==0)):
                    return False
                if(len(domain_dict[x_i])>1):
                    neighbors = [x for x in self.get_neighbors(state,x_i[0],x_i[1]) if x[0]!=x_j[0] and x[1] != x_j[1] ]
                    for x_k in neighbors:
                        arc.append((x_k,x_i))
                        
                
                elif(len(domain_dict[x_j])>1):
                    neighbors = [x for x in self.get_neighbors(state,x_j[0],x_j[1]) if x[0]!=x_i[0] and  x[1] != x_i[1] ]
                    for x_k in neighbors:
                        arc.append((x_k,x_j))  
                      
        return domain_dict

    def remove_inconsistancy_value(self,position1, position2):
        removed = False
        d_i= domain_dict[position1]
        d_j= domain_dict[position2]
        if(len(d_i) == 1 and len(d_i) <= len(d_j)):
            d_j_before = d_j
            d_j = [x for x in d_j if x not in d_i]
            if (d_j==d_j_before):
                removed = False
            else:
                domain_dict[position2] = d_j
                removed = True
        elif(len(d_j) == 1 and len(d_j) <= len(d_i)):
            d_i_before = d_i
            d_i = [x for x in d_i if x not in d_j]
            if (d_i==d_i_before):
                removed = False
            else:
                domain_dict[position1] = d_i
                removed = True
        return removed
     
            
    def get_neighbors(self,state,row,col):
        empty_cell_array = self._get_empty_cells(state)
        empty_neighbor = [x for x in list(set(self._gen_arcs(row, col)).intersection(empty_cell_array)) if x != (row,col)]
        return empty_neighbor
    
    def _gen_arcs(self,row, col):
        moves = []
        col_moves = self.getColIndexArray(col)
        block_moves = self.getBlockIndexArray(row, col)
        row_moves = [(row, x) for x in range(9)]
        moves.extend(row_moves)
        moves.extend(block_moves)
        moves.extend(col_moves)
        return list(set(moves))
    
    def getColIndexArray(self,col_num):
        col = []
        for row in range(9):
            col.append((row,col_num))
        return col

    def getBlockIndexArray(self,row, col):
        block = []
        row = row - row%3
        col = col - col%3
        for i in range(3):
            for j in range(3):
                block.append((i+row,j+col))
        return block
        


def main():

    easy_boards = getEasyBoards()
    medium_boards = getMediumBoards()
    hard_boards = getHardBoards()

     
    backtrack = BackTrack()
    for board in medium_boards:
        starting_state = State(board, None, None)  
        starting_state.genBoard()
        backtrack.AC3(starting_state)
        print("doing AC3")
        backtrack.backtrack(starting_state)
        print('\n')
        starting_state.genBoard()
        
        t= input("here")
        
        
        
main()

