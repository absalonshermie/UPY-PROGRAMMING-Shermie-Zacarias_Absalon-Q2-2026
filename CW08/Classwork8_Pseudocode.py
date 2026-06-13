#INPUT
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

#PROCESS
area <- 0.0
n <- 1000
h <- (b - a) / n
shift <- 0
constant <- 0

IF method is equal "RRM"
    shift <- 1
ENDIF

IF method is equal "MPM"
    constant <- h / 2
ENDIF

IF method is equal "TRP"
    shift <- 1
ENDIF

FOR i IN RANGE (0 + shift, n + shift) DO
    xi <- a + i * h + constant
    
    height <- f_x (xi)
    
    IF method is equal "TRP"
        area <- area + 2 * height * h
    ELSE
        area <- area + height * h
    ENDIF
ENDFOR

IF method is equal "TRP"
    fa <- f_x (a)
    fb <- f_x (b)
    area <- (area + (fa * h) + (fb * h)) / 2
ENDIF

#OUTPUT
DISPLAY " The integration of " + f_x + " is " + area