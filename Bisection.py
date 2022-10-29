def bisectionM(function1, a , b ):
    faa = function1(a)
    fbb = function1(b)

    if faa * fbb > 0:
        print("function1 a and function b  must have different signs !")
        return None

    for _ in range(50):
        m = (a + b) / 2
        fcc = function1(m)

        if fcc == 0:
            return m
        if faa * fcc > 0:
            a = m
            faa = fcc
        if fbb * fcc > 0:
            b = m
            fbb = fcc

    return m


fcc = lambda x: x**4 - 2 * x

a=1
b=3
print(f"Interval {a,b}")
x = bisectionM(fcc, a, b)
print("last mid-point is :")
print(x)
