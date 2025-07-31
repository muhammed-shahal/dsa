def main():
    print("LCM")

# Logic -> LCM * HCF = x * y
def lcm(x, y):
    gcd = None
    product = x*y

    while x > 0 and y > 0:
        if x>=y:
            x = x%y
        else:
            y = y%x
    
    if x == 0:
        gcd = y
    else:
        gcd = x
    
    return product // gcd
    