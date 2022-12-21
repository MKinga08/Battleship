def game_board():
    board = []
    rows, cols = 10, 10
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append("0")
        board.append(col)
    return board


def print_gameboard(board):
    print("    A", " B", " C", " D", " E", " F", " G", " H", " I", " J")
    counter = 0
    for i in board:
        collector = ""
        row = " "
        counter += 1
        for k in i:
            if counter <= 9:
                collector += k + "  "
            else:
                row = ""
                collector += k + "  "
        print(counter, row, collector)


def ship_input():
    print("In this game you have 13 ships which have different lengths\nYour ships are the following:")
    ships = [0, 5, 3, 3, 2]
    for i in range(len(ships)-1, 0, -1):
        print(f"{ships[i]}pc of {i} unit long ship")
    print("Enter a beginner and an end coordinate for all of your ships")
    for j in range(len(ships)-1, 0, -1):
        print(f"Place your {j} unit length ships:")
        pcs = ships[j]
        while pcs > 0:
            first = input("First coordinate:")
            last = input("Second coordinate:")
            #validation
            pcs -= 1


def users_input(columns):
    print("You can place your ships by typing in a letter and a number like this: A1")
    while True:
        place = input("Where would you like to place your ship?:").upper()
        col = place[0]
        if len(place) == 2:
            row = place[1]
        else:
            row = place[1] + place[2]
        if col.isalpha():
            if col not in columns:
                print("Letter out of range")
            else:
                if row.isnumeric():
                    if int(row) > 10:
                        print("Number out of range")
                    else:
                        return col, row
                else:
                    print("The second part of the coordinate must be a number")
        else:
            print("The first part of the coordinate must be a letter")


def coordinates(col, row, columns):
    for i in range(len(columns)):
        if col == columns[i]:
            col = i
            return col, row


def placing_ships(col, row, board):
    col = int(col)
    row = int(row) - 1
    if board[row][col] == "0":
        board[row][col] = "X"


def main():
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    gboard = game_board()
    while True:
        print_gameboard(gboard)
        ship_input()
        col, row = users_input(columns)
        col, row = coordinates(col, row, columns)
        placing_ships(col, row, gboard)


if __name__ == "__main__":
    main()
