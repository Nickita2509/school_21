import math

def pascal(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

try:
    n = int(input())
    if n <= 0:
        print("Natural number was expected")
    else:
        list1 = []
        for i in range(n):
            list2 = []
            for j in range(i+1):
                list2.append(pascal(i,j))
            list1.append(list2)

        for _ in range(n):
            print(*list1[_])
except ValueError:
    print("Natural number was expected")
