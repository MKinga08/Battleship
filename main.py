def game_board():
    board = []
    rows, cols = 5, 5
    print("   A", " B", " C", " D", " E")
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append("0")
        board.append(col)
    return board


def print_gameboard(board):
    counter = 0
    for i in board:
        collector = " "
        counter += 1
        for k in i:
            collector += k + "  "
        print(counter, collector)


def users_input():
    print("You can place your ships by typing in a letter and a number like this: A1")
    while True:
        place = input("Where would you like to place your ship?:").upper()
        if place[0].isnumeric():
            print("First you have to type in a letter")
        elif place[1].isalpha():
            print("You have to type in a number for the second coordinate")
        elif place[0].isalpha() and place[1].isnumeric():
            return place
        else:
            print("You have to type in a letter than a number")


def coordinates(place):
    columns = ["A", "B", "C", "D", "E"]
    for i in range(len(columns)):
        if place[0] == columns[i]:
            place = str(i) + place[1]
            return place


def main():
    gboard = game_board()
    print_gameboard(gboard)
    userinput = users_input()
    coordinates(userinput)


if __name__ == "__main__":
    main()
