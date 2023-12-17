def count(lst):
    s = 0
    for i in lst:
        if isinstance(i, list):
            s += count(i) + 1
        else:
            s += 1
    return s


def calculate_xi(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    return ((n - 1) * calculate_xi(n - 1)) / 3 + ((n - 2) * calculate_xi(n - 2)) / 4


print(count([]))
print(count([1, 2, 3]))
print(count(["x", "y", ["z"]]))
print(count([1, 2, [3, 4, [5]]]))
print(calculate_xi(1))
print(calculate_xi(2))

    