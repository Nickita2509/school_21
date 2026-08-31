a = input().split()
aa = [float(i) for i in a]
b = input().split()
bb = [float(i) for i in b]
ab = aa[0] * bb[0] + aa[1] * bb[1] + aa[2] * bb[2]
print(ab)