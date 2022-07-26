def add_last1(m, n):
    m += n

t1 = (1, 3)
add_last1(t1, (5, 7))
print(t1)


def add_last2(m, n):
    m += n
    return m

t2 = (1, 3)
t2 = add_last2(t2, (5, 7))
print(t2)
