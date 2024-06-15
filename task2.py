#1
x = 3
y = 3
while 1:
    if x + y > 0:
        x -= 2
        y += 1
    else:
        break
print(f"Y = {y}")

#2
a = 5
b = 5
while 1:
    if b > 0:
        b -= 1
        a = a * 2 + 1
    else:
        break
print(f"A = {a}")

#3
a = 1
s = 0
p = 0
while 1:
    if a > 10:
        break
    else:
        a += 2
        p += a
        s += p
print(f"S = {s}")

#4
for x in range(5, -6, -1):
    y = 2 * x + 1
    print("End" if y < 1 else "Continue")

#5
for x in range(5, -16, 2):
    for y in range(5, 15):
        print("Continue" if x + y > 0 else "End")

#6
s = 1
for n in range(1, 6):
    s *= n
print(f"S = {s}")

#7
k = [0] * 11
l = [0] * 11
for i in range(1, 11):
    k[i] = 10 - i
for i in range(1, 11):
    l[i] = k[5] - k[i]
for i in range(1, len(l)):
    x += 1
print(x)

#8
m = 12
n = 5
while 1:
    if m == n:
        break
    else:
        if m > n:
            m = m - 2 * n
        else:
            n -= 3
print(f"M = {m}")

#9
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = b ** 2 - 4 * a * c
print(f"b^2 - 4ac > 0: {d > 0}")
import math
D = math.sqrt(d)
print(f"D > 0: {D > 0}")
x1 = (-b + D) / 2 * a
x2 = (-b - D) / 2 * a
print(f"X1 = {x1} X2 = {x2}")