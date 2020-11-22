import math
import os
import time
runs = 0
print(f"1: do not hit enter until you have entered something\nthe machine will tell if if the answer is impossible")
while True:
    if runs > 0:
        cs = input("enter 0 to clear screen else enter anything: ")
        if cs == "0":
            print("wait a second there is an error try alt f4")
            time.sleep(3)
            os.system('cls')
    print("POKEMON LETS GO")
    print("wait a second")
    time.sleep(3)
    print("ok now")
    time.sleep(.5)
    runs += 1
    verywrong = 0
    vc = 0
    ca = [0, 0]
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    ln = float(input("ln: "))
    oa = a
    ob = b
    oc = c
    oln = round(ln, 3)
    ln = ln - c
    b = b / a
    c = c / a
    ln = ln / a
    nc = (b / 2) ** 2
    ln = (nc + ln)
    if nc > 0:
        nc = math.sqrt(nc)
    else:
        print("False black bear")
    if ln > 0:
        ln = math.sqrt(ln)
    else:
        print("False black bear")
    if nc > 0:
        if ln > 0:
            x1 = round(((ln * -1) - nc), 3)
            x2 = round((ln - nc), 3)
            aa1 = (round(((oa * (x1 ** 2)) + (ob * x1) + oc), 3))
            aa2 = (round((oa * ((x1 * -1) ** 2) + (ob * (x1 * -1)) + oc), 3))
            aa3 = (round(((oa * (x2 ** 2)) + (ob * x2) + oc), 3))
            aa4 = (round(((oa * ((x2 * -1) ** 2)) + (ob * (x2 * -1)) + oc), 3))
            m1 = oln - 1
            m2 = oln + 1
            if m1 <= aa1 <= m2:
                print(x1)
                ca.insert(0, x1)
                vc += 1
            else:
                verywrong += 1
            if m1 <= aa2 <= m2:
                print(x1 * -1)
                if vc == 0:
                    ca.insert(0, (x1 * -1))
                else:
                    ca.insert(1, (x1 * -1))
                vc += 1
            else:
                verywrong += 1
            if m1 <= aa3 <= m2:
                print(x2)
                if vc == 0:
                    ca.insert(0, x2)
                else:
                    ca.insert(1, x2)
                vc += 1
            else:
                verywrong += 1
            if m1 <= aa4 <= m2:
                print(x2 * -1)
                if vc == 0:
                    ca.insert(0, (x2 * -1))
                else:
                    ca.insert(1, (x2 * -1))
                vc += 1
            else:
                verywrong += 1
            if verywrong == 4:
                print("oopsy doopsie we made a mistake")
            else:
                print("wow it worked")
            showwork = input("enter s to show work else enter anything: ")
            if showwork == "s":
                print(f"{oa}x^2 + {ob}x = {(oln - oc)}")
                print(f"x^2 + {(ob / oa)} = {(oln - oc) / oa}")
                print(f"x^2 + {(ob / oa)} = {(oln - oc) / oa}\n       _  = {((ob / oa) / 2)}\n       2")
                print(f"{((ob / oa) / 2)}^2 = {((ob / oa) / 2) ** 2}")
                print(f"x^2 + {ob / oa}x + {((ob / oa) / 2) ** 2} = {((oln - oc) / oa) + ((ob / oa) / 2) ** 2}")
                n1 = math.sqrt(((ob / oa) / 2) ** 2)
                if (ob / oa) < 0:
                    if (((ob / oa) / 2) ** 2) < 0:
                        print(f"(x + {n1})^2 = {(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                        b1 = math.sqrt(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)
                        print(f"x + {n1} = +/-{math.sqrt(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                if (ob / oa) < 0:
                    if (((ob / oa) / 2) ** 2) > 0:
                        print(f"(x + -{n1})^2 = {(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                        print(f"x + {n1} = +/-{math.sqrt(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                if (ob / oa) > 0:
                    if (((ob / oa) / 2) ** 2) < 0:
                        print(f"(x + -{n1})^2 = {(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                        print(f"x + {n1} = +/-{math.sqrt(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                if (ob / oa) > 0:
                    if (((ob / oa) / 2) ** 2) > 0:
                        print(f"(x + {n1})^2 = {(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                        print(f"x + {n1} = +/-{math.sqrt(((oln - oc) / oa) + ((ob / oa) / 2) ** 2)}")
                print(f"the answers are {ca[0]} and {ca[1]}")
                print("HAHA nerd")
            else:
                print("next")