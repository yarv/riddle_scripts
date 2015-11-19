""" A set of functions to deal with knights tour problems

"""

import operator

import math

def allowed_pos(pos, board, movenum): 

    moves = [(i,j) for i in [-1,1,-2,2] for j in [-1,1,-2,2] if
    abs(j)!= abs(i)]   
    
    allowed_pos = [tuple(map(operator.add,pos,move)) for move in
    moves]  

    allowed_pos = [x for x in allowed_pos if all(coord >=0 and
    coord<=7 for coord in x)]  
    
    allowed_pos = [x for x in allowed_pos if board[x] == 0]
    
    if movenum != 63: 
        allowed_pos = [x for x in allowed_pos if x != (2,1)] 
       
    return allowed_pos

def print_board(board, writefile): 

    board_size = int(math.sqrt(len(board))) 
    scale = len(str(len(board)))

    
    
    writefile.write(board_size*("+" + scale*"-") + "+\n") 

    for i in range(board_size): 
        for j in range(board_size):
            writefile.write("|%*d" % (scale, board[(i,j)]))

        writefile.write("|\n"+ board_size*("+" + scale*"-") + "+\n")
        
    writefile.write("\n") 




def tour_search(current_pos, current_board, answers, movenum, limit):

    cur_board = current_board.copy() 
    cur_board[current_pos] = movenum

    if len(answers) >= limit: 
        return answers

    elif movenum == 64:

        print("Tour found!")  
        answers.append(cur_board)


        
    elif len(allowed_pos(current_pos,cur_board,movenum)) == 0:

        print("bogus path, trying again")
        cur_board[current_pos] = 0


    else: 
        next_pos = [(len(allowed_pos(pos, cur_board,movenum+1)),pos)
        for pos in allowed_pos(current_pos,cur_board,movenum)] 

        next_pos.sort()
        
        next_pos = [pos for (length,pos) in next_pos]

        for pos in next_pos: 
            tour_search(pos, cur_board, answers, movenum+1, limit) 


def print_answers(answerlist, filename):
    answerfile = open(filename, 'w')
    
    answerfile.write("A list of " + str(len(answerlist)) + " closed")
    answerfile.write(" knight's tours:\n")
    answerfile.write("\n")
    
    for board in answerlist:
        print_board(board, answerfile)
    
    answerfile.close()


if __name__ == "__main__":
    initial_pos = (0,0) 
    limit = 1000

    initial_board = {(i,j):0 for i in range(8) for j in range(8)}
    initial_board[initial_pos] = 1
    
    answers = []

    tour_search(initial_pos, initial_board, answers,1, limit)
    
    print(str(limit) + " tours found, printing results to file")

    print_answers(answers, "closedknightstoursolns.txt")
        
