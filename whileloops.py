a = 50
b = 20


while b > 0:
    a, b = b, a % b
    ## tmp = a
    ## a = b
    ## b = tmp % b

print (a)