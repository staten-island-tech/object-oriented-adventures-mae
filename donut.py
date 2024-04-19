def lowest_triangle():
    a = float(input("Area: "))
    b = float(input("Base: "))
    if a < 1 or a > 1000000:
        print("Error")
    if b < 1 or b > 1000000:
        print("Error")
    else:
        h = a/(0.5 * b)
        print(h)


lowest_triangle()