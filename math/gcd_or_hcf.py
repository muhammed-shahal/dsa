def main():
    print("GCD or HCF")

    print(f"GCD of 4, 6 is: {gcd(4, 6)}")

def gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x = x %y
        else:
            y = y % x
    
    if x == 0:
        return y
    
    return x

if __name__ == "__main__":
    main()