def h(a, b, c):
    d = a + b + c
    print("Total:", d)
    if d > 100000:
        print("Diskon 10%")
        d = d - (d * 0.1)
    print("Bayar:", d)

h(50000, 30000, 40000)