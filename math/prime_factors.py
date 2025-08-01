def main():
    print("Prime Factors")
    print("Prime Factors of 900")
    prime_factors(900)
    print("Prime Factors of 35")
    prime_factors(35)

def prime_factors(num):
    i = 2

    while i*i <= num:
        while num % i == 0:
            print(i)
            num = num // i
        i += 1
    
    if num > 1:
        print(num)
if __name__ == "__main__":
    main()