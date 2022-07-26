l = [3, 1, 5, 4, 7, 6]
def min_max(a):
    a.sort()
    print(a[0], a[-1], sep = ' , ')


min_max(l)


def min_max2(a):
    a = list(a)
    a.sort()
    print(a[0], a[-1], sep = ', ')

min_max2(l)
print(l)

c = (3, 1, 5, 4, 7, 6)
min_max2(c)
print(c)


    
