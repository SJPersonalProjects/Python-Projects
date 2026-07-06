# Tic Tac Toe Board Printer.

board = {
    "top-left": " ",
    "top-middle": " ",
    "top-right": " ",
    "middle-left": " ",
    "middle-middle": " ",
    "middle-right": " ",
    "bottom-left": " ",
    "bottom-middle": " ",
    "bottom-right": " "
}

# Printing board.
print(board["top-left"] + " | " + board["top-middle"] + " | " + board["top-right"])
print("--+---+--")
print(board["middle-left"] + " | " + board["middle-middle"] + " | " + board["middle-right"])
print("--+---+--")
print(board["bottom-left"] + " | " + board["bottom-middle"] + " | " + board["bottom-right"])