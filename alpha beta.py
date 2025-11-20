# alphabeta_tictactoe.py
import math

def check_win(b,p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in w) for w in wins)

def aval(b): return [i for i,v in enumerate(b) if v==' ']

def alphabeta(b, ai, maximizing, alpha, beta):
    opp = 'O' if ai=='X' else 'X'
    if check_win(b, ai): return (1, None)
    if check_win(b, opp): return (-1, None)
    moves=aval(b)
    if not moves: return (0, None)
    if maximizing:
        best = (-math.inf, None)
        for m in moves:
            b[m]=ai
            score,_ = alphabeta(b, ai, False, alpha, beta)
            b[m]=' '
            if score>best[0]: best=(score,m)
            alpha = max(alpha, score)
            if beta<=alpha: break
        return best
    else:
        best = (math.inf, None)
        for m in moves:
            b[m]=opp
            score,_ = alphabeta(b, ai, True, alpha, beta)
            b[m]=' '
            if score<best[0]: best=(score,m)
            beta = min(beta, score)
            if beta<=alpha: break
        return best

def ai_move(b, ai): return alphabeta(b, ai, True, -math.inf, math.inf)[1]

if __name__=="__main__":
    board = [' ']*9
    print("AlphaBeta move:", ai_move(board,'X'))
