numbers = "insert numbers here"
# ORDER: AA-AA / AA-Aa / AA-aa / Aa-Aa / Aa-aa / aa-aa
num = numbers.split(" ")
prob = (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])* 0.75 + int(num[4])* 0.5 + int(num[5]) * 0) * 2
print(prob)