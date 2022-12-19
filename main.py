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


def main():
    gboard = game_board()
    print_gameboard(gboard)


if __name__ == "__main__":
    main()
