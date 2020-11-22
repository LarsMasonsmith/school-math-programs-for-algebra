def veryeasysoup():
  a9 = float(input("A: "))
  x8 = float(input("x1: "))
  y8 = float(input("y1: "))
  R = (y8 / a9)**-x8
  answer6666 = ("f(x)= " + a9 + "(" + R + ")^x")
  print(answer6666)
  minnesota = float(input("do you whish to plug in a value   to this equation if so enter 1 else enter 5: "))
  if minnesota == 5:
    homescreen()
  while minnesota == 1:
    newx666 = float(input("what x value do you inquire: "))
    newanswer666 = a9 * (R**newx666)
    print(newanswer666)
def easysoup():
  r2 = float(input("R: "))
  x21 = float(input("x1: "))
  y21 = float(input("y1: "))
  if x21 == 0:
    answer = ("f(x)=" + r2 + "(" + y21 + ")^x")
  else:
    x321 = x21 * -1
    A21 = (y21 * r2)**x321
    answer = ("f(x)=" + A21 + "(" + r2 + ")^x")
  print(answer)
  ohnos = float(input("do you whish to plug in a value   to this equation if so enter 1 else enter 5: "))
  if ohnos == 5:
    homescreen()
  while ohnos == 1:
    newx21 = float(input("what x value do you inquire: "))
    print((newx21**r2) * A21)
    ohnos = float(input("do you whish to plug in a value   to this equation if so enter 1 else enter 5: "))
def easyish():
  x1 = float(input("x1: "))
  y1 = float(input("y1: "))
  x2 = float(input("x2: "))
  y2 = float(input("y2: "))
  if x2 - x1 == 1:
    R = y2 / y1
  else:
    soop = float(y2 / y1)
    soup = float(1 / (x2 - x1))
    R = soop**soup
  if x1 == 0:
    A = y1
  else:
    suop = R**-x1
    A = y1 * suop
  suup = "f(x) = " + str(A) + "(" + str(R) + ")^x"
  print(suup)
  coop = float(input("do you whish to plug in a value   to this equation if so enter 1 else enter 5: "))
  if coop == 5:
    homescreen()
  while coop == 1:
    xv = float(input("what x value do you inquire: "))
    souop = R**xv
    newanswer = A * souop
    print(newanswer)
    coop = float(input("do you whish to plug in values   to this equation if so enter 1 else enter 5 for home: "))
    if coop == 5:
      homescreen()
def easy():
  A1 = float(input("enter the staring amount:"))
  R1 = float(input("enter the rate"))
  print("f(x)=" + str(A1) + "(" + str(R1) + ")^x")
  surup = float(input("do you whish to plug in a value   to this equation if so enter 1 else enter 5: "))
  if surup == 5:
    homescreen()
  while surup == 1:
    newX1 = float(input("enter the xvalue you inquire: "))
    soop1 = R1**newX1
    print(A1 * soop1)
    surup = float(input("do you whish to plug in values   to this equation if so enter 1 else enter 5 for home: "))
    if surup == 5:
      homescreen()
def homescreen():
  print("you are in the home screen enter  if you have the following information enter 1 else enter 0")
  q1 = float(input("do you know x1: "))
  q2 = float(input("do you know y1: "))
  q3 = float(input("do you know x2: "))
  q4 = float(input("do you know y2: "))
  q5 = float(input("do you know the rate: "))
  q6 = float(input("do you know the starting amount"))
  if q1 + q2 + q3 + q4 == 4 and q5 != 1 and q6 != 1:
    easyish()
  if q5 == 1 and q6 == 1:
    easy()
  if q1 + q2 + q3 + q4 == 3 or 2 and q5 == 1 and q6 != 1:
    easysoup()
  if q1 + q2 + q3 + q4 == 3 or 2 and q5 != 1 and q6 == 1:
    veryeasysoup()
homescreen()