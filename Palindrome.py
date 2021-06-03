# brute force approach using recursion
def checkPalindrome_1(string, k):
    length = len(string)
    return (rec_checkPalindrome_1(string, 0, length) <= 2 * k)


def rec_checkPalindrome_1(string, m, n):
    # m starts at 0 index and works toward the end
    # if m has reached the end, return n
    if m == (len(string)):
        return n
    # n starts at the end of the string and works toward the beginning
    # if n reaches the beginning, return length - m
    if not n:
        return (len(string) - m)

    # if the elements at the two current indices match,
    # they do not need to be removed.
    # just move each to the next element and continue
    if string[m] == string[n - 1]:
        return rec_checkPalindrome_1(string, m + 1, n - 1)

    # if the elements at the two current indices do not match,
    # one of them needs to be removed.  Try both and use whichever ends
    # up with the lowest count
    result = 1 + min(rec_checkPalindrome_1(string, m + 1, n),
                     rec_checkPalindrome_1(string, m, n - 1))
    return result


# top-down dynamic programming approach with memoization
def checkPalindrome_2(string, k):
    length = len(string)
    # initialize empty memo to hold values
    memo = {}
    return (rec_checkPalindrome_2(string, memo, 0, length) <= 2*k)


def rec_checkPalindrome_2(string, memo, m, n):
    # check memo to see if the current problem has already been solved
    # if so, return the corresponding value
    if (m, n) in memo:
        return memo[(m, n)]

    # if m has reached the end of the string, add the current value
    # of n to the memo with the current (m,n) tuple and return n
    if m == (len(string)):
        memo[(m, n)] = n
        return n

    # if n has reached the beginning of the string, add the current
    # difference between m and the end of the string to the memo and
    # return the same value
    if not n:
        memo[(m, n)] = (len(string) - m)
        return memo[(m, n)]

    # if the characters at the two indices match, recursively call
    # the function with incremented/decremented m and n values and
    # insert the result in the memo and return.
    if string[m] == string[n - 1]:
        memo[(m, n)] = rec_checkPalindrome_2(string, memo, m + 1, n - 1)
        return memo[(m, n)]

    # if the characters do not match, use the minimum value obtained by
    # twp separate recursive calls, one incrementing m, the other
    # decrementing n, add one and store in the memo and return.
    memo[(m, n)] = 1 + min(rec_checkPalindrome_2(string, memo, m + 1, n),
                           rec_checkPalindrome_2(string, memo, m, n - 1))
    return memo[(m, n)]


string = "abccblav"
k = 2
print(checkPalindrome_2(string, k))
