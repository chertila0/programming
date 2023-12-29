
def rec_count(lst):
    s = 0
    for i in lst:
        if isinstance(i, list):
            s += count(i) + 1
        else:
            s += 1
    return s


def rec_calculate_xi(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    return ((n - 1) * rec_calculate_xi(n - 1)) / 3 + ((n - 2) * rec_calculate_xi(n - 2)) / 4


print(rec_count([]))
print(rec_count([1, 2, 3]))
print(rec_count(["x", "y", ["z"]]))
print(rec_count([1, 2, [3, 4, [5]]]))

for i in range(1, 11):
    print(rec_calculate_xi(i))


    