def count(l):
    k = len(l)
    a = 0
    if k:
        for i in l:
            if i is list:
                a += count(i)
            else:
                a += 1
    else:
        return 0
    return k+a
print(count([1,[2,8, []]]))