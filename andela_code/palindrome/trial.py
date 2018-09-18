def power(n, e):
    t = 1
    for _ in range(e):
        t = t * n
    return t


print(power(2, 3))
print(power(2, 0))
