import heapq

def getTesla(M):
    rows = len(M)
    cols = len(M[0])
    # totals list to keep track of the cumulative total of each element plus the previous elements in its optimal path
    totals = [[-float('inf') for i in range(cols)] for j in range(rows)]
    totals[0][0] = M[0][0]
    # lowest list keeps track of the lowest health number in the path
    lowest = [[-float('inf') for i in range(cols)] for j in range(rows)]
    lowest[0][0] = M[0][0]

    # create priority queue using negative m[row][col] so that it pops the highest instead of lowest
    q = [(-M[0][0], 0, 0)]
    # per instructions Mr x can only move down or right:
    moves = [(1,0),(0,1)]
    while len(q) > 0:
        room_health, row, col = heapq.heappop(q)
        # check the right neighbor and down neighbor:
        for row_move, col_move in moves:
            neighbor_row, neighbor_col = row + row_move, col + col_move
            # make sure the neighbor is valid
            if (neighbor_row < rows and neighbor_col < cols):
                # if the neighbor's lowest value can be raised by moving it to the current path, adjust its values
                # in totals and lowest where appropriate
                if lowest[row][col] > lowest[neighbor_row][neighbor_col]:
                    totals[neighbor_row][neighbor_col] = totals[row][col] + M[neighbor_row][neighbor_col]
                    lowest[neighbor_row][neighbor_col] = min(totals[neighbor_row][neighbor_col], lowest[row][col])
                    heapq.heappush(q, (-M[neighbor_row][neighbor_col], neighbor_row, neighbor_col))
                elif lowest[row][col] == lowest[neighbor_row][neighbor_col]:
                    totals[neighbor_row][neighbor_col] = max(totals[neighbor_row][neighbor_col], totals[row][col] - M[neighbor_row][neighbor_col])
                    heapq.heappush(q, (-M[neighbor_row][neighbor_col], neighbor_row, neighbor_col))
    # the bottom right element of the lowest matrix contains the lowest total value within the optimal path.
    # This is usually going to be negative, so subtract it from 1 to get the minimum health points needed.
    # IF the value is positive, that would result in a negative health value which is not allowed, so return 1 instead
    return max(1, 1-lowest[rows-1][cols-1])

M = [[-1,-2,2],
     [10,-8,1],
     [-5,-2,-3]]

print(getTesla(M))