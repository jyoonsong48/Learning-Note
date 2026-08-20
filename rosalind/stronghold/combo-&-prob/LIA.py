import math

data = "insert numbers here"
dataset = data.split(" ")
k = int(dataset[0]) # number of generation
n = int(dataset[1]) # program wil calculate the probablity: at least n number of AaBbs

def mendel_2_prob(k, n):
    offspring = 2 ** k
    sum_prob = 0
    for i in range(0, n):
        combo = math.comb(offspring, i)
        AaBb = (0.25)**i
        non_AaBb = (0.75)**(offspring - i)
        current_prob = combo * AaBb * non_AaBb
        sum_prob = sum_prob + current_prob
    return (1-sum_prob)

print(mendel_2_prob(k,n))

