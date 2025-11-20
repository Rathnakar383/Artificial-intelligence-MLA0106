# minimax_tictactoe.py
import math

def check_win(b,p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in w) for w in wins)

def available_moves(b): return [i for i,v in enumerate(b) if v==' ']

def minimax(b, player, maximizing):
    opponent = 'O' if player=='X' else 'X'
    if check_win(b, player): return (1, None)
    if check_win(b, opponent): return (-1, None)
    moves = available_moves(b)
    if not moves: return (0, None)
    if maximizing:
        best = (-math.inf, None)
        for m in moves:
            b[m]=player
            score,_ = minimax(b, player, False)
            b[m]=' '
            if score > best[0]:
                best=(score,m)
        return best
    else:
        best = (math.inf, None)
        for m in moves:
            b[m]=opponent
            score,_ = minimax(b, player, True)
            b[m]=' '
            if score < best[0]:
                best=(score,m)
        return best

def minimax_ai_move(b, ai_player):
    score, move = minimax(b, ai_player, True)
    return move

if __name__=="__main__":
    board = [' ']*9
    # Example: AI plays X on empty board
    move = minimax_ai_move(board, 'X')
    print("AI move:", move)
