import re
with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

data = dataset.split(">")
sequences = [item for s in data for item in re.split(r'Rosalind_\d+\n', s) if item]
sequences = [item.replace("\n", "") for item in sequences]

def edit(str1, str2):
    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
    dp[0] = list(range(0, (len(str2)+1)))
    for i in range(0, len(str1)+1):
        dp[i][0] = i
    for k in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[k-1] == str2[j-1]:
                dp[k][j] = dp[k-1][j-1]
            else:
                dp[k][j] = min(dp[k-1][j-1], dp[k-1][j], dp[k][j-1]) + 1
    #for row in dp:
    #    print(row)
    return dp[len(str1)][len(str2)]

print(edit(sequences[0], sequences[1]))
