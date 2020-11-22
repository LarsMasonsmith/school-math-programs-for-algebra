while 3 > 1:
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    if x1 == x2:
        print("x = " + str(x1))
    elif y1 == y2:
        print("y =" + str(y1))
    else:
        yd = (y1 - y2)
        xd = (x1 - x2)
        unit_rate = (yd / xd)
        Psy = (y1 * - 1)
        if Psy >= 0:
            Psy = ("+ " + str(Psy))
        Psx = (x1 * - 1)
        if Psx >= 0:
            Psx = ("+ " + str(Psx))
        yintercept = (x1 * (-1 * unit_rate) + y1)
        yp = (yintercept)
        if yp >= 0:
            yp = ("+ " + str(yp))
        print("colin's weird point slope form: y = " + str(unit_rate) + "(x " + str(Psx) + ") + " + str(y1))
        print("standard form: y = " + str(unit_rate) + "x " + str(yp))
        print("normal slope intercept form: y " + str(Psy) + "= " + str(unit_rate) + "(x -" + str(x1) + ")")

