def patternmatch(string, p):
    cache = [[0 for i in range(len(p)+1)] for j in range(len(string)+1)]
    m = 0
    n = 0
    while m < len(p) and n < len(string):
        