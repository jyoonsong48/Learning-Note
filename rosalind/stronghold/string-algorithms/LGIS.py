with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

dataset = data.split("\n")
n = dataset[0]
del dataset[0]
seq = [int(char) for item in dataset for char in item.split(" ")]


def inc_substring(seq):
    dp = []
    for i in range(len(seq)):
        looking = seq[i]
        candidates = []
        for j in range(i):
            if looking > dp[j][-1]:
                candidates.append(dp[j]) 
        if candidates:
            best = max(candidates, key=len)
            dp.append(best[:] + [looking])
        else:
            dp.append([looking])
    return dp

longest_inc = max(inc_substring(seq), key=len)


def dec_substring(seq):
    dp = []
    for i in range(len(seq)):
        looking = seq[i]
        candidates = []
        for j in range(i):
            if looking < dp[j][-1]:
                candidates.append(dp[j]) 
        if candidates:
            best = max(candidates, key=len)
            dp.append(best[:] + [looking])
        else:
            dp.append([looking])
    return dp

longest_dec = max(dec_substring(seq), key=len)

with open("substring.txt", "w") as f:
    for item in longest_inc:
        f.write(f"{item} ")
    f.write("\n")
    for item in longest_dec:
        f.write(f"{item} ")


