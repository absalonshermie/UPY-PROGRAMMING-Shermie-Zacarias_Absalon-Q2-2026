import math

#INPUT
a = input( "Write the left endopoint of the interval: ")
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)
b = input( "Write the right endopoint of the interval: ")
if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)
    
f_x = input("Write the function to integrate")
method = input("Select integration method (LRM/RRM/MPM/TRP)")

#PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
    
if method == "MPM":
    constant = h/2

if method == "TRP":
    shift = 1

for i in range(0 + shift, n + shift):
    xi = a + i * h + constant
    
    x = xi
    height = eval(f_x)
    if method == "TRP":
        area += 2 * height * h
    else:
        area += height * h
        
if method == "TRP":
    x = a
    fa = eval(f_x)
    x = b
    fb = eval(f_x)
    area = (area + (fa * h) + (fb * h)) / 2
    
#OUTPUT
print(f" The integration of {f_x} is {area:.4f}")