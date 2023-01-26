board = []
ships_data = []
cant_place_ships = []
player = ""


def game_board():
    origin_board = []
    rows, cols = 10, 10
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append("0")
        origin_board.append(col)
    return origin_board


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
    print(f"Its your turn, {player}")


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
                        ships_data.append([coord])
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
    if len(place) == 1:
        print("Invalid coordinate")
    else:
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
                    ships_data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
            else:
                if coord2[0] - coord1[0] == j - 1:
                    for i in range(coord1[0], coord2[0] + 1):
                        temp_data.append((i, coord1[1]))
                    ships_data.append(sorted(temp_data))
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
                    ships_data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
            else:
                if coord2[1] - coord1[1] == j - 1:
                    for i in range(coord1[1], coord2[1] + 1):
                        temp_data.append((coord1[0], i))
                    ships_data.append(sorted(temp_data))
                    cant_place_ships_coordinates(coord1, coord2)
                    place_ships()
                else:
                    print("Ship too long or ship too small")
                    pcs += 1
    print_game_board()
    return pcs


def place_ships():
    for list_coord in ships_data:
        for coord in list_coord:
            if board[coord[0]][coord[1]] == "0":
                board[coord[0]][coord[1]] = "X"


def cant_place_ships_coordinates(coord1, coord2):
    if coord1[1] != coord2[1]:
        if coord1[1] > coord2[1]:
            coord3 = coord2
            coord2 = coord1
            coord1 = coord3
        for lists in ships_data:
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
        for lists in ships_data:
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
        for i in ships_data:
            if k == i:
                return True
    return False


def get_player():
    player1 = input("Who is the first player?")
    player2 = input("Who is the second player?")
    return player1, player2


def change_player(player1, player2):
    global player
    return player1 if player1 != player else player2


def change_board(board1, board2):
    global board
    return board1 if board1 != board else board2


def change_ships_data(ships_data1, ships_data2):
    global ships_data
    return ships_data1 if ships_data1 != ships_data else ships_data2


def change_cant_place_ships(cant_place_ships1, cant_place_ships2):
    global cant_place_ships
    return cant_place_ships1 if cant_place_ships1 != cant_place_ships else cant_place_ships2


def change_round(player1, player2, board1, board2, ships_data1, ships_data2, cant_place_ships1, cant_place_ships2):
    global player, board, cant_place_ships, ships_data
    player = change_player(player1, player2)
    board = change_board(board1, board2)
    ships_data = change_ships_data(ships_data1, ships_data2)
    cant_place_ships = change_cant_place_ships(cant_place_ships1, cant_place_ships2)


def input_validation_for_shooting(columns, place):
    if len(place) == 1:
        print("Invalid coordinate")
    else:
        col, row = col_row(place)
        if col.isalpha():
            if col not in columns:
                print("Letter out of range")
            else:
                if row.isnumeric():
                    if int(row) > 10 or int(row) <= 0:
                        print("Number out of range")
                    else:
                        return True
                else:
                    print("The second part of the coordinate must be a number")
        else:
            print("The first part of the coordinate must be a letter")


def print_shoot_game_board():
    global board
    shoot_board = board
    for i in shoot_board:
        for k in range(len(i)):
            if i[k] == "X":
                i[k] = "0"
    print("    A", " B", " C", " D", " E", " F", " G", " H", " I", " J")
    counter = 0
    for lists in shoot_board:
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


def shooting(columns, player1, player2, board1, board2, ships_data1, ships_data2, cant_place_ships1, cant_place_ships2):
    global ships_data
    global board
    ships_data = change_ships_data(ships_data1, ships_data2)
    board = change_board(board1, board2)
    while True:
        print_shoot_game_board()
        print(f"It's your turn to shoot {player}")
        shoot = input("Enter a coordinate to shoot:").upper()
        if input_validation_for_shooting(columns, shoot):
            col, row = col_row(shoot)
            shoot = coordinates(col, row, columns)
            if any(shoot in sublist for sublist in ships_data):
                if board[shoot[0]][shoot[1]] == "0":
                    board[shoot[0]][shoot[1]] = "H"
                for sublist in ships_data:
                    for i in sublist:
                        if i == shoot:
                            sublist.remove(i)
                print("Hit")
            else:
                if board[shoot[0]][shoot[1]] == "0":
                    board[shoot[0]][shoot[1]] = "M"
                print("No ship on that position")
            ship_sinking()
            check_winner()
            change_round(player1, player2, board1, board2, ships_data1, ships_data2, cant_place_ships1, cant_place_ships2)


def ship_sinking():
    count4 = 0
    for i in range(0, 2):
        if len(ships_data[i]) == 0:
            count4 += 1
    if count4 > 0:
        print(f"You sunk {count4} four-length ship!")
    count3 = 0
    for k in range(2, 5):
        if len(ships_data[k]) == 0:
            count3 += 1
    if count3 > 0:
        print(f"You sunk {count3} three-length ship!")
    count2 = 0
    for j in range(5, 8):
        if len(ships_data[j]) == 0:
            count2 += 1
    if count2 > 0:
        print(f"You sunk {count2} two-length ship!")
    count1 = 0
    for a in range(8, 13):
        if len(ships_data[a]) == 0:
            count1 += 1
    if count1 > 0:
        print(f"You sunk {count1} one-length ship!")


def check_winner():
    if not any(ships_data):
        print(f"Congratulations {player}, You sunk all the ships!")
        quit()


def main():
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    ships = [5, 3, 3, 2]
    global player, board, ships_data, cant_place_ships
    board1, board2 = game_board(), game_board()
    board = board1
    player1, player2 = get_player()
    player = player1
    ships_data1, ships_data2 = [], []
    ships_data = ships_data1
    cant_place_ships1, cant_place_ships2 = [], []
    cant_place_ships = cant_place_ships1
    print_game_board()
    for rounds in range(2):
        beginning(ships)
        ship_input(ships, columns)
        change_round(player1, player2, board1, board2, ships_data1, ships_data2, cant_place_ships1, cant_place_ships2)
        if player == player2:
            print_game_board()
    # shooting_phase
    shooting(columns, player1, player2, board1, board2, ships_data1, ships_data2, cant_place_ships1, cant_place_ships2)


if __name__ == "__main__":
    main()
