def patternmatch(string, p):
    plength = len(p)
    slength = len(string)
    cache = [[0 for i in range(plength)] for j in range(slength)]
    for i in range(slength):
        for j in range(plength):
            if p[j] == '*':
                if i == 0 or cache[i-1][j] or cache[i][j-1]:
                    cache[i][j] = 1
            elif p[j] == '?':
                if j == 0:
                    if i == 0:
                        cache[i][j] == 1

                elif i > 1:
                    cache[i][j] = cache[i-1][j-1]
                elif p[j-1] == '*':
                    cache[i][j] = cache[i-1][j]
            elif p[j] == i[j]:
                cache[i][j] = cache[i-1][j-1]