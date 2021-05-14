def is_valid_ic(ic_str):
    # force string to uppercase
    ic_str = ic_str.upper()

    # a valid IC must have 10 characters
    if len(ic_str) != 10:
        return False

    # the first character of a valid IC must be 'T'
    if ic_str[0] != 'T':
        return False

    # characters 1..8 must be digits
    try:
        # convert characters to numbers
        a, b, c, d, e, f, g, h = [int(i) for i in ic_str[1:9]]
    except ValueError:
        # some character is not a digit
        return False

    # last character must match checksum
    checksum = (2 * a + 7 * b + 6 * c + 5 * d + 4 * e + 3 * f + 2 * g + h + 4) % 11
    return ic_str[9] == "ZJIHGFEDCBA"[checksum]

def main():
    s = input("Please enter an IC (starting with T): ")

    if is_valid_ic(s):
        print("IC is valid")
    else:
        print("IC is not valid")

if __name__=="__main__":
    main()
