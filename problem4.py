import math
import random
import string


def clean_message(message):
    result = ""

    for ch in message.upper():
        if ch.isalpha():
            result = result + ch

    return result


def make_grid(message, rows, cols):
    while len(message) < rows * cols:
        message = message + random.choice(string.ascii_uppercase)

    grid = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        grid.append(row)

    return grid


def make_path(rows, cols):
    path = []

    for c in range(cols):
        if c % 2 == 0:
            for r in range(rows):
                path.append((r, c))
        else:
            for r in range(rows - 1, -1, -1):
                path.append((r, c))

    return path


def encode(message):
    rows = 5
    cols = math.ceil(len(message) / rows)

    message = clean_message(message)

    grid = make_grid(message, rows, cols)
    path = make_path(rows, cols)

    cipher = ""

    for location in path:
        r, c = location
        cipher = cipher + grid[r][c]

    return cipher


def decode(cipher):
    rows = 5
    cols = math.ceil(len(cipher) / rows)

    path = make_path(rows, cols)

    grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("")
        grid.append(row)

    index = 0

    for location in path:
        r, c = location
        grid[r][c] = cipher[index]
        index += 1

    message = ""

    for r in range(rows):
        for c in range(cols):
            message = message + grid[r][c]

    return message


def main():
    choice = input("Encode or decode? ")

    if choice.lower() == "encode":
        message = input("Enter the message: ")
        print("Ciphertext:", encode(message))
    else:
        cipher = input("Enter the ciphertext: ")
        print("Message:", decode(cipher))


main()
