def main():
    print("Reverse a Number")

    print(f"Rverse of 123 is: {reverse_a_number(123)}")

    print(f"Reverse of 121 if: {reverse_a_number(121)}")

def reverse_a_number(num):
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    
    return reverse

if __name__ == "__main__":
    main()