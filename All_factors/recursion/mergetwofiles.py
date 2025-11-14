f1 = open("file1.txt")
f2 = open("file2.txt")
out = open("merged.txt", "w")

l1 = f1.readlines()
l2 = f2.readlines()

for a, b in zip(l1, l2):
    out.write(a)
    out.write(b)

f1.close()
f2.close()
out.close()
