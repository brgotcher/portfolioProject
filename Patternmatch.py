def patternmatch(string, p):
    plength = len(p)
    slength = len(string)
    # set up cache to build bottom-up table
    cache = [[0 for i in range(plength+1)] for j in range(slength+1)]
    # fill in the cache
    for i in range(slength+1):
        for j in range(plength+1):
            # extra row and column included to simplify looking back when on first row or column
            # [0][0] must be 1 so that the first comparison of characters will return 1 if they match
            if i == 0 and j == 0:
                cache[i][j] = 1
            # keep the rest of the first column at 0
            elif j == 0:
                cache[i][j] = 0
            # rest of first row 0 unless corresponding char in p is * and the previous position holds a 1
            elif i == 0:
                if p[j-1] == '*' and cache[i][j-1]:
                    cache[i][j] = 1
            # if the current element of p holds *, it will be a match if either previous value of i or j was a match
            elif p[j-1] == '*':
                if cache[i][j-1] or cache[i-1][j]:
                    cache[i][j] = 1
            # if the current element of p is a '?' or if it is equal to the current element of string, it is a match if
            # the previous elements were a match
            elif p[j-1] == '?' or p[j-1] == string[i-1]:
                cache[i][j] = cache[i-1][j-1]
    return bool(cache[slength][plength])

p = "*?B*C?E*"
string = "ABCDE"
print(patternmatch(string, p))