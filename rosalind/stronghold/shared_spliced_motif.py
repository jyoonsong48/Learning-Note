import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]
# print(sequences)
def common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # for row in dp:
    #    print(row)
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            j -= 1
        else:
            i -= 1
    return "".join(reversed(lcs))

longest_inc = common_substring(sequences[0], sequences[1])

print(longest_inc)

