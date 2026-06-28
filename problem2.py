def make_board():
    board = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "K"],
        ["L", "M", "N", "O", "P"],
        ["Q", "R", "S", "T", "U"],
        ["V", "W", "X", "Y", "Z"]
    ]

    return board


def find_letter(board, letter):
    if letter == "J":
        letter = "I"

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == letter:
                return (row + 1, col + 1)


def encode(message, board):
    code = ""

    for letter in message.upper():
        if letter.isalpha():
            location = find_letter(board, letter)
            code = code + str(location[0]) + str(location[1]) + " "

    return code


def decode(code, board):
    message = ""

    pairs = code.split()

    for pair in pairs:
        row = int(pair[0]) - 1
        col = int(pair[1]) - 1
        message = message + board[row][col]

    return message


def main():
    board = make_board()

    choice = input("Encode or decode? ")

    if choice.lower() == "encode":
        message = input("Enter a message: ")
        print("Encoded message:", encode(message, board))
    else:
        code = input("Enter the code with spaces between pairs: ")
        print("Decoded message:", decode(code, board))


main()
