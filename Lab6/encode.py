# Matthew Bajdas

def encode(password):
    encoded_password = ""
    print("Your password has been encoded and stored!\n")
    for num in password:
        encoded_password += str((int(num) + 3) % 10)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""

    for num in encoded_password:
        decoded_password += str((int(num) - 3) % 10)

    return decoded_password


def main():
    while True:
        print(f"Menu"), print("-" * 13), print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}. \n")
        elif option == 3:
            break


if __name__ == "__main__":
    main()
