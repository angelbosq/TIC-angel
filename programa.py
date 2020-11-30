def programa():
    n =0
    x = input("x=")
    m  = 0
    for i in range(0,10):
        if (i%3) == 0:
            n = n + i
        else:
            m = m + i
    print n, m

programa()
