n = int(input())

if n < 0:
    print(False)
else:
    t = n 
    d = 0

    while n != 0:
        temp = n % 10
        n = n // 10
        d += temp 
        d *= 10
        
    d = d // 10
    print (d == t)