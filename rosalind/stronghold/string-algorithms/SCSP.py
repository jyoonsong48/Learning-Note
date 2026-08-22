import re
with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

str1, str2 = dataset.split("\n")

# print(str1, str2)

def SCSP(str1, str2):
    m, n = len(str1), len(str2)
# dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# filling dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:          # match
                dp[i][j] = dp[i-1][j-1] + 1
            else:                               # match X
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    result = []
    i = m
    j = n          # begins from bottom right

    while i > 0 and j > 0:
        if  str1[i-1] == str2[j-1]:              # match -> move diagonally
            result.append(str1[i-1])         # append once
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:    # upper value >= -> move up
            result.append(str1[i-1])         # append
            i -= 1
        else:                              # left value >= -> move left
            result.append(str2[j-1])         # append
            j -= 1


    while i > 0:                # str1 is longer
        result.append(str1[i-1])
        i -= 1

    while j > 0:                # str2 is longer
        result.append(str2[j-1])
        j -= 1


    result.reverse()
    scs = "".join(result)
    return scs

print(SCSP(str1, str2))