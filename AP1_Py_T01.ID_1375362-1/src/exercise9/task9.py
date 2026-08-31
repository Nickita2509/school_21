parts = input().split()
n = int(parts[0])
x = float(parts[1])
coeffs = [float(input()) for _ls in range(n + 1)]
d = 0
coeffs.reverse()

for i in range(1,len(coeffs)):
    d += coeffs[i] * i * x ** (i - 1)

print(f"{d:.3f}")
