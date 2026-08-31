def check_format(l):
    flag = True
    if l[0] not in ['+', '-']:
       flag = False
    else:
        if "." in l:
            if l.count(".") != 1:
                flag = False
            else:
                if l.index(".") < 2 or l.index(".") == len(l) - 1:
                    flag = False
    if flag:
        for i in range(1, len(l)):
            if l[i] == '.' or l[i].isdigit():
                 flag = True
            else:
                 flag = False
                 break
    return flag

s = input()
flag = check_format(s)
if flag:
    sym = s[0]
    s1 = s[1:]
 
    d1 = 0
    d2 = 0
    for i in range(len(s1)):
        if s1[i] == '.':
            break
        else:
            d1 = d1 * 10 + (ord(s1[i]) - ord('0'))     

    if "." in s1:
        dot_index = s1.index(".")
        frac_len = len(s1) - dot_index - 1 
        for i in range(s1.index(".") + 1, len(s1)):
            d2 = d2 * 10 + (ord(s1[i]) - ord('0'))

        d2 = d2 / (10 ** frac_len)

    d = (d1 + d2) / 1 * 2

    if s[0] == '-':
        d = d * -1
    print(f"{d:.3f}")
else:
    print("ERROR")

