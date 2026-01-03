def main():
    print("GCD and LCM")

    print("GCD of 4 and 6 is:", gcd(4, 6))
    print("GCD of 100 and 200 is:", gcd(100, 200))
    print("GCD of 7 and 13 is:", gcd(7, 13))

    print("LCM of 4 and 6:", lcm(4, 6))
    print("LCM of 12 and 15:", lcm(12, 15))
    print("LCM of 2 and 8:", lcm(2, 8))


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

def lcm(a, b):
    hcf = gcd(a, b)

    return (a*b)// hcf

if __name__ == "__main__":
    main()