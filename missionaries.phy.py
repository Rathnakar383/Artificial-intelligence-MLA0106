from collections import deque

def is_valid(state):
    M_left, C_left, boat, M_right, C_right = state
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False
    if (M_left and M_left < C_left) or (M_right and M_right < C_right):
        return False
    return True

def missionaries_and_cannibals():
    start = (3, 3, 1, 0, 0)
    goal = (0, 0, 0, 3, 3)
    q = deque([(start, [start])])

    while q:
        state, path = q.popleft()
        if state == goal:
            for step in path:
                print(step)
            return

        M_left, C_left, boat, M_right, C_right = state
        moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

        for m, c in moves:
            if boat == 1:
                new_state = (M_left - m, C_left - c, 0, M_right + m, C_right + c)
            else:
                new_state = (M_left + m, C_left + c, 1, M_right - m, C_right - c)

            if is_valid(new_state):
                q.append((new_state, path + [new_state]))

missionaries_and_cannibals()
