import cmath
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b:" ))
c=float(input("Enter the value of c:"))
d=(b*b)-(4*a*c)
if(d>0):
  r1 = (-b + cmath.sqrt(d)) / (2 * a)
  r2 = (-b - cmath.sqrt(d)) / (2 * a)
  print("The roots are real and different",r1,r2)
elif(d==0):
  r1 = r2 = -b / 2 * a
  print("roots are real and  equal", r1)
else:
  real = -b / (2 * a)
  img = cmath.sqrt(d) / (2 * a)
  print("complex roots", real, "+", img, "and", real, "-", img)