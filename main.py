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
        col, row = users_input(columns)
        col, row = coordinates(col, row, columns)
        placing_ships(col, row, gboard)


if __name__ == "__main__":
    main()
