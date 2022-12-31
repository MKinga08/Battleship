board = []
data = []
cant_place_ships = []


def game_board():
    rows, cols = 10, 10
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append("0")
        board.append(col)
    return board


def print_game_board():
    print("    A", " B", " C", " D", " E", " F", " G", " H", " I", " J")
    counter = 0
    for lists in board:
        collector = ""
        row = " "
        counter += 1
        for elements in lists:
            if counter <= 9:
                collector += elements + "  "
            else:
                row = ""
                collector += elements + "  "
        print(counter, row, collector)


def beginning(ships):
    print("In this game you have 13 ships which have different lengths\nYour ships are the following:")
    for i in range(len(ships), 0, -1):
        print(f"{ships[i - 1]}pc of {i} unit long ship")
    print("You can place your ships by typing in a letter and a number like this: A1")
    print("Enter a beginner and an end coordinate for all of your ships")


def ship_input(ships, columns):
    for ship_length in range(len(ships), 0, -1):
        print(f"Place your {ship_length} unit length ships:")
        pcs = ships[ship_length - 1]
        while pcs > 0:
            while True:
                if ship_length == 1:
                    one_unit = input("Give a coordinate to your 1 unit length ship:").upper()
                    if input_validation(columns, one_unit):
                        col, row = col_row(one_unit)
                        coord = coordinates(col, row, columns)
                        data.append([coord])
                        cant_place_one_unit_ships_coordinates(coord)
                        place_ships()
                        print_game_board()
                        break
                else:
                    first = input("First coordinate?:").upper()
                    if input_validation(columns, first):
                        col, row = col_row(first)
                        coord1 = coordinates(col, row, columns)
                        last = input("Second coordinate?:").upper()
                        if input_validation(columns, last):
                            col, row = col_row(last)
                            coord2 = coordinates(col, row, columns)
                            pcs = generate_ships(coord1, coord2, pcs, ship_length)
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
    col, row = col_row(place)
    if col.isalpha():
        if col not in columns:
            print("Letter out of range")
        else:
            if row.isnumeric():
                if int(row) > 10 or int(row) <= 0:
                    print("Number out of range")
                else:
                    coord = coordinates(col, row, columns)
                    if board[coord[0]][coord[1]] == "X" or coord in cant_place_ships:
                        print("Position taken or ships too close")
                    else:
                        return True
            else:
                print("The second part of the coordinate must be a number")
    else:
        print("The first part of the coordinate must be a letter")
    return False


def col_row(place):
    col = place[0]
    if len(place) == 2:
        row = place[1]
    else:
        row = place[1] + place[2]
    return col, row


def generate_ships(coord1, coord2, pcs, j):
    temp_data = []
    if coord1[0] != coord2[0] and coord1[1] != coord2[1]:
        print("There is no such ship")
        pcs += 1
    else:
        if coord1[0] != coord2[0]:
            if coord1[0] > coord2[0]:
                if coord1[0] - coord2[0] == j - 1:
                    for i in range(coord2[0], coord1[0] + 1):
                        temp_data.append((i, coord1[1]))
                    data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
            else:
                if coord2[0] - coord1[0] == j - 1:
                    for i in range(coord1[0], coord2[0] + 1):
                        temp_data.append((i, coord1[1]))
                    data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
        elif coord1[1] != coord2[1]:
            if coord1[1] > coord2[1]:
                if coord1[1] - coord2[1] == j - 1:
                    for i in range(coord2[1], coord1[1] + 1):
                        temp_data.append((coord2[0], i))
                    data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
            else:
                if coord2[1] - coord1[1] == j - 1:
                    for i in range(coord1[1], coord2[1] + 1):
                        temp_data.append((coord1[0], i))
                    data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
    print_game_board()
    return pcs


def place_ships():
    for list_coord in data:
        for coord in list_coord:
            if board[coord[0]][coord[1]] == "0":
                board[coord[0]][coord[1]] = "X"


def cant_place_ships_coordinates(coord1, coord2):
    if coord1[1] != coord2[1]:
        if coord1[1] > coord2[1]:
            coord3 = coord2
            coord2 = coord1
            coord1 = coord3
        for lists in data:
            for k in lists:
                cant_place_ships.append((k[0] - 1, k[1]))
                cant_place_ships.append((k[0] + 1, k[1]))
            cant_place_ships.append((coord1[0], coord1[1] - 1))
            cant_place_ships.append((coord2[0], coord2[1] + 1))
            cant_place_ships.append((coord1[0] - 1, coord1[1] - 1))
            cant_place_ships.append((coord1[0] + 1, coord1[1] - 1))
            cant_place_ships.append((coord2[0] - 1, coord2[1] + 1))
            cant_place_ships.append((coord2[0] + 1, coord2[1] + 1))
    else:
        if coord1[0] > coord2[0]:
            coord3 = coord2
            coord2 = coord1
            coord1 = coord3
        for lists in data:
            for tuples in lists:
                cant_place_ships.append((tuples[0], tuples[1] - 1))
                cant_place_ships.append((tuples[0], tuples[1] + 1))
            cant_place_ships.append((coord1[0] - 1, coord1[1]))
            cant_place_ships.append((coord2[0] + 1, coord2[1]))
            cant_place_ships.append((coord1[0] - 1, coord1[1] - 1))
            cant_place_ships.append((coord1[0] - 1, coord1[1] + 1))
            cant_place_ships.append((coord2[0] + 1, coord2[1] - 1))
            cant_place_ships.append((coord2[0] + 1, coord2[1] + 1))


def cant_place_one_unit_ships_coordinates(coord):
    cant_place_ships.append((coord[0], coord[1] - 1))
    cant_place_ships.append((coord[0], coord[1] + 1))
    cant_place_ships.append((coord[0] - 1, coord[1]))
    cant_place_ships.append((coord[0] + 1, coord[1]))
    cant_place_ships.append((coord[0] + 1, coord[1] - 1))
    cant_place_ships.append((coord[0] + 1, coord[1] + 1))
    cant_place_ships.append((coord[0] - 1, coord[1] - 1))
    cant_place_ships.append((coord[0] - 1, coord[1] + 1))


def cant_place():
    for k in cant_place_ships:
        for i in data:
            if k == i:
                return True
    return False


def main():
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    ships = [5, 3, 3, 2]
    game_board()
    print_game_board()
    beginning(ships)
    ship_input(ships, columns)


if __name__ == "__main__":
    main()
