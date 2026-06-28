import math
import random
import string


def clean_message(message):
    result = ""

    for ch in message.upper():
        if ch.isalpha():
            result = result + ch

    return result


def make_grid(message, columns):
    rows = math.ceil(len(message) / columns)

    while len(message) < rows * columns:
        message = message + random.choice(string.ascii_uppercase)

    grid = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(message[index])
            index = index + 1
        grid.append(row)

    return grid


def keyword_order(keyword):
    letters = []

    for i in range(len(keyword)):
        letters.append((keyword[i], i))

    letters.sort()

    order = [0] * len(keyword)

    for number in range(len(letters)):
        original_column = letters[number][1]
        order[original_column] = number + 1

    return order


def encode(message, keyword):
    message = clean_message(message)
    keyword = clean_message(keyword)

    grid = make_grid(message, len(keyword))
    order = keyword_order(keyword)

    cipher = ""

    for number in range(1, len(keyword) + 1):
        col = order.index(number)

        for row in range(len(grid)):
            cipher = cipher + grid[row][col]

        cipher = cipher + " "

    return cipher


def decode(cipher, keyword):
    keyword = clean_message(keyword)
    cipher = clean_message(cipher)

    columns = len(keyword)
    rows = len(cipher) // columns

    order = keyword_order(keyword)

    grid = []

    for r in range(rows):
        row = []
        for c in range(columns):
            row.append("")
        grid.append(row)

    index = 0

    for number in range(1, columns + 1):
        col = order.index(number)

        for row in range(rows):
            grid[row][col] = cipher[index]
            index = index + 1

    message = ""

    for row in range(rows):
        for col in range(columns):
            message = message + grid[row][col]

    return message


def main():
    choice = input("Encode or decode? ")
    keyword = input("Enter the keyword: ")

    if choice.lower() == "encode":
        message = input("Enter the message: ")
        print("Ciphertext:", encode(message, keyword))
    else:
        cipher = input("Enter the ciphertext: ")
        print("Message:", decode(cipher, keyword))


main()
