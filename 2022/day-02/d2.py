# d2.py
# Advent of Code - Day 2 - wyattboyer
from y2022 import aocUtils

# rock = 1, paper = 2, scissors = 3 (index + 1), win = 6pts, draw = add both, loss = 0pts
STRAT = ['s', 'p', 'r'] # mod 3 ring, 3, 2, 1
STRATS = {'r':1, 'p':2, 's':3} # point equivs
P1_KEY = {'A':'r', 'B':'p', 'C':'s','X':'r', 'Y':'p', 'Z':'s'}
P2_KEY = {'A':'r', 'B':'p', 'C':'s', 'X':0, 'Y':3, 'Z':6}

# P1
# The corresponding strategy is found for each key, then results are determined
# wins are decided by STRAT where a strategy beats another if it directly precedes it within
# the ring (mod 3), therefore index mod 3 determines win
def exec_strat(strat: list[tuple[str]]) -> int:
    score = 0
    for (S1, S2) in strat:
        score += pts(S2)
        if ndx(S1) == ndx(S2) : # draw
            score += 3
        elif (ndx(S2)+1)%3 == ndx(S1): # win
            score += 6
    return score

# P2
# X = 0pts (lose), Y = 3pts (draw), Z = 6pts (win)
# if win, move +2 mod3 in index
# if draw, pick the same 
# if lose, move +1 mod3 in index
def calc_strat(strat: list[tuple[str]]) -> int:
    score = 0
    for (S1, S2) in strat:
        score += P2_KEY[S2]
        print(f"{S1}:{ndx(S1)} - ", end="")
        if P2_KEY[S2] == 6 :
            move = STRAT[(ndx(S1)+2)%3]
            score += STRATS[STRAT[(ndx(S1)+2)%3]]
            print(f"{S2}: win  - choice: {STRAT.index(move)}:{move} -- running score: {score}")
        elif P2_KEY[S2] == 3:
            move = STRAT[ndx(S1)]
            score += pts(S1)
            print(f"{S2}: draw - choice: {STRAT.index(move)}:{move} -- running score: {score}")
        else:
            move = STRAT[(ndx(S1)+1)%3]
            score += STRATS[STRAT[(ndx(S1)+1)%3]]
            print(f"{S2}: loss  - choice: {STRAT.index(move)}:{move} -- running score: {score}")
    return score      

def ndx(s: str) -> int:
    return STRAT.index(P1_KEY[s])

def pts(s: str) -> int:
    return STRATS[P1_KEY[s]]

def format_data(raw: str) -> list[tuple[str]]:
    arr = raw.split()
    return [(arr[i-1], arr[i]) for i in range(1, len(arr), 2)]

if __name__=='__main__':
    file = 'input.txt'
    raw = raw_text(file)
    data = format_data(raw)
    res1 = exec_strat(data)
    res2 = calc_strat(data)
    print(f"Part 1 Score: {res1}\nPart 2 Score: {res2}\n")

    
