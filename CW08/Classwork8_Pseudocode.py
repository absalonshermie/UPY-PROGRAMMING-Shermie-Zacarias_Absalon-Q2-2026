# INPUT
Get a, b, f_x, method from user
IF a contains "pi"
    a <- value of pi
ELSE
    a <- convert a to float
ENDIF

IF b contains "pi"
    b <- value of pi
ELSE
    b <- convert b to float
ENDIF

# PROCESS
area <- 0.0
n <- 1000
h <- (b - a) / n
shift <- 0
constant <- 0
variable <- 0

IF method is equal "TRAP"
    variable <- 1
    
    f_0 <- f_x(a)
    area <- area + (h / 2) * f_0
    
    FOR i IN RANGE (variable, n) DO
        xi <- a + (i * h)
        f_xi <- f_x(xi)
        area <- area + (h / 2) * 2 * f_xi
    ENDFOR
    
    f_xn <- f_x(b)
    area <- area + (h / 2) * f_xn
ENDIF

IF method is equal "RRM"
    shift <- 1
ENDIF

IF method is equal "MPM"
    constant <- h / 2
ENDIF

IF method is not equal "TRAP"
    FOR i IN RANGE (0 + shift, n + shift) DO
        xi <- a + (i * h) + constant
        
        height <- f_x(xi) 
        area <- area + height * h
    ENDFOR
ENDIF

# OUTPUT
DISPLAY " The integration of " + f_x + " is " + area