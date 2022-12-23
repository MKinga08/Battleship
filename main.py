
board = []


def game_board():
    rows, cols = 10, 10
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append("0")
        board.append(col)
    return board


def print_gameboard():
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


def beginning(ships):
    print("In this game you have 13 ships which have different lengths\nYour ships are the following:")
    for i in range(len(ships) - 1, 0, -1):
        print(f"{ships[i]}pc of {i} unit long ship")
    print("You can place your ships by typing in a letter and a number like this: A1")
    print("Enter a beginner and an end coordinate for all of your ships")


def ship_input(ships, columns):
    data = []
    for j in range(len(ships) - 1, 0, -1):
        print(f"Place your {j} unit length ships:")
        pcs = ships[j]
        while pcs > 0:
            while True:
                first = input("First coordinate?:").upper()
                if input_validation(columns, first):
                    col, row = colrow(first)
                    coord1 = coordinates(col, row, columns)
                    last = input("Second coordinate?:").upper()
                    if input_validation(columns, last):
                        col, row = colrow(last)
                        coord2 = coordinates(col, row, columns)
                        if coord1[0] != coord2[0] and coord1[1] != coord2[1]:
                            print("There is no such ship")
                            pcs += 1
                        else:
                            if coord1[0] != coord2[0]:
                                if coord1[0] > coord2[0]:
                                    if coord1[0] - coord2[0] == j-1:
                                        for i in range(coord2[0], coord1[0] + 1):
                                            data.append((i, coord1[1]))
                                    else:
                                        print("Ship too long or ship too small")
                                        pcs += 1
                                else:
                                    if coord2[0] - coord1[0] == j-1:
                                        for i in range(coord1[0], coord2[0] + 1):
                                            data.append((i, coord1[1]))
                                    else:
                                        print("Ship too long or ship too small")
                                        pcs += 1
                            elif coord1[1] != coord2[1]:
                                if coord1[1] > coord2[1]:
                                    if coord1[1] - coord2[1] == j-1:
                                        for i in range(coord2[1], coord1[1] + 1):
                                            data.append((coord2[0], i))
                                    else:
                                        print("Ship too long or ship too small")
                                        pcs += 1
                                else:
                                    if coord2[1] - coord1[1] == j-1:
                                        for i in range(coord1[1], coord2[1] + 1):
                                            data.append((coord1[0], i))
                                    else:
                                        print("Ship too long or ship too small")
                                        pcs += 1
                        print(data)
                        break
            pcs -= 1



def coordinates(col, row, columns):
    for i in range(len(columns)):
        if col == columns[i]:
            col = i
    col = int(col)
    row = int(row) - 1
    store_data = (row, col)
    return store_data


def input_validation(columns, place):
    col, row = colrow(place)
    if col.isalpha():
        if col not in columns:
            print("Letter out of range")
        else:
            if row.isnumeric():
                if int(row) > 10 or int(row) <= 0:
                    print("Number out of range")
                else:
                    coord = coordinates(col, row, columns)
                    if board[coord[0]][coord[1]] == "X":
                        print("Position taken")
                    else:
                        return True
            else:
                print("The second part of the coordinate must be a number")
    else:
        print("The first part of the coordinate must be a letter")
    return False


def colrow(place):
    col = place[0]
    if len(place) == 2:
        row = place[1]
    else:
        row = place[1] + place[2]
    return col, row


#def generate_ships():

def main():
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    ships = [0, 5, 3, 3, 2]
    game_board()
    while True:
        print_gameboard()
        beginning(ships)
        ship_input(ships, columns)


if __name__ == "__main__":
    main()
