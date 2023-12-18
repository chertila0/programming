def count(lst):
    stack = lst
    count = 0
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
            count += 1
        else:
            count += 1
    return count

def calculate_xi(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    xi_2 = 1
    xi_1 = -1 / 8
    xi = 0
    for i in range(3, n+1):
        xi = ((i - 1) * xi_1) / 3 + ((i - 2) * xi_2) / 4
        xi_2 = xi_1
        xi_1 = xi
    return xi

for i in range(1, 11):
    print(calculate_xi(i))


    