def func (x, y):
    return x ** y

def func2 (x, y):
    r = 1 / x
    for i in range(-y - 1):
        r *= r
    return r


x = 5
y = -2
print(str(func(x,y)))
print(str(func2(x,y)))
