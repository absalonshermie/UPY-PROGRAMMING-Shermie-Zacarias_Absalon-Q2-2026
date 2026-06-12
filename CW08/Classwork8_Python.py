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
    b = float(a)
    
f_x = input("Write the function to integrate")
method = input("Select integration method (LRM/RRM/MPM)")

#PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0
variable = 0

if method == "TRAP":
    variable = 1
    
    f_0 = f_x.replace("x", f"({a})")
    area += (h/2) * eval(f_0)
    
    for i in range(variable, n):
        xi = a + (i * h)
        f_xi = f_x.replace("x", f"({xi})")
        area += (h/2) * 2 * eval(f_xi)
        
    f_xn = f_x.replace("x", f"({b})")
    area += (h/2) * eval(f_xn) 

if method == "RRM":
    shift = 1
    
if method == "MPM":
    constant = h/2
else:
    pass

for i in range(0 + shift, n + shift):
    xi = a + i * h + constant
    
    height = eval(f_x.replace("x", str(xi)))
    area += height * h
    
#OUTPUT
print(f" The integration of {f_x} is {area:.4f}") 