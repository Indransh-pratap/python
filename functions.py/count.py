s = input("Enter text: ").lower()
v = "aeiou"
count = sum(1 for ch in s if ch in v)
print("Vowel Count =", count)
