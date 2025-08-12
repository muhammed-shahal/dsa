import math

def main():
    print("Number of Set Bits")

    print(f"Number of Set bits is 42 {number_of_set_bits(42)}")


def number_of_set_bits(num):
    count = 0

    while num != 0:
        num = num & num -1
        count += 1

    return count

if __name__ == "__main__":
    main()