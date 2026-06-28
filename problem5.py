import math
import random
import string


def clean_message(message):
    result = ""

    for ch in message.upper():
        if ch.isalpha():
            result = result + ch

    return result


def create_grid(message, rows, cols):
    while len(message) < rows * cols:
        message += random.choice(string.ascii_uppercase)

    grid = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        grid.append(row)

    return grid


def get_keyword_order(keyword):
    keyword = keyword.upper()

    letters = []

    for i in range(len(keyword)):
        letters.append((keyword[i], i))

    letters.sort()

    order = []

    for item in letters:
        order.append(item[1])

    return order


def encode(message, keyword):
    message = clean_message(message)
    keyword = clean_message(keyword)

    cols = len(keyword)
    rows = math.ceil(len(message) / cols)

    grid = create_grid(message, rows, cols)
    order = get_keyword_order(keyword)

    cipher = ""

    for col in order:
        for row in range(rows):
            cipher += grid[row][col]

    return cipher


def decode(cipher, keyword):
    cipher = clean_message(cipher)
    keyword = clean_message(keyword)

    cols = len(keyword)
    rows = len(cipher) // cols

    order = get_keyword_order(keyword)

    grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("")
        grid.append(row)

    index = 0

    for col in order:
        for row in range(rows):
            grid[row][col] = cipher[index]
            index += 1

    message = ""

    for row in grid:
        for letter in row:
            message += letter

    return message


def main():
    print("Keyword Cipher")

    choice = input("Encode or decode? ").lower()
    keyword = input("Enter keyword: ")

    if choice == "encode":
        message = input("Enter message: ")
        print("Ciphertext:", encode(message, keyword))
    elif choice == "decode":
        cipher = input("Enter ciphertext: ")
        print("Decoded message:", decode(cipher, keyword))
    else:
        print("Invalid choice.")


main()
