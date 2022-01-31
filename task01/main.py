def calc():
    x = float(input("Укажите числитель: "))
    y = float(input("Укажите знаменатель: "))
    if y != 0:
        d = x / y
        print(d)
    else:
        print('Something wrong with Y')
    

calc()