def mergesort(a):
    if len(a) == 1:
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            return [a[1], a[0]]
        else:
            return a

    p = len(a)//2
    m1 = mergesort(a[:p])

