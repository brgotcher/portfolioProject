# brute force approach using recursion
def checkPalindrome_1(string, k):
    length = len(string)
    return (rec_checkPalindrome_1(string, 0, length) <= 2*k)
def rec_checkPalindrome_1(string, m, n):
    # m starts at 0 index and works toward the end
    # if m has reached the end, return n
    if m == (len(string)):
        return n
    # n starts at the end of the string and works toward the beginning
    # if n reaches the beginning, return length - m
    if not n:
        return (len(string)) - m

    # if the elements at the two current indices match,
    # they do not need to be removed.
    # just move each to the next element and continue
    if string[m] == string[n-1]:
        return rec_checkPalindrome_1(string, m+1, n-1)

    # if the elements at the two current indices do not match,
    # one of them needs to be removed.  Try both and use whichever ends
    # up with the lowest count
    result = 1 + min(rec_checkPalindrome_1(string, m+1, n), rec_checkPalindrome_1(string, m, n-1))
    return result

string = "ablcba"
k = 1
print(checkPalindrome_1(string, k))