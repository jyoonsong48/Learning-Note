vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
inp = input("Input:")
out = ''.join([char for char in inp if char not in vowels])
print(f"Output: {out}")

