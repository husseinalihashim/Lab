board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def show_board():
    print("\n  a b c d e f g h")
    for r in range(8):
        rank = 8 - r
        print(f"{rank} {' '.join(board[r])} {rank}")
    print("  a b c d e f g h\n")

def parse_pos(pos):
    if len(pos) != 2:
        return None
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    if 0 <= col <= 7 and 0 <= row <= 7:
        return row, col
    return None

def get_color(piece):
    if piece == '.':
        return None
    return 'white' if piece.isupper() else 'black'

def is_valid_pawn_move(sr, sc, er, ec, piece):
    color = get_color(piece)
    target = board[er][ec]
    direction = -1 if color == 'white' else 1
    start_row = 6 if color == 'white' else 1

    if sc == ec and target == '.':
        if er == sr + direction:
            return True
        if sr == start_row and er == sr + (2 * direction) and board[sr + direction][sc] == '.':
            return True

    if abs(sc - ec) == 1 and er == sr + direction:
        if target != '.' and get_color(target) != color:
            return True

    return False

turn = 'white'

while True:
    show_board()
    print(f"Turn: {turn}")
    move = input("Move (e.g. e2e4) or 'q' to quit: ").strip().lower()

    if move == 'q':
        break
    if len(move) != 4:
        print("Invalid format! Use 4 characters like e2e4.")
        continue

    start = parse_pos(move[:2])
    end = parse_pos(move[2:])

    if not start or not end:
        print("Invalid coordinates!")
        continue

    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    target = board[er][ec]

    if piece == '.':
        print("No piece at that position!")
        continue

    if get_color(piece) != turn:
        print(f"It's {turn}'s turn! You cannot move that piece.")
        continue

    if target != '.' and get_color(target) == turn:
        print("Cannot capture your own piece!")
        continue

    if piece.lower() == 'p':
        if not is_valid_pawn_move(sr, sc, er, ec, piece):
            print("Invalid move for pawn!")
            continue

    board[er][ec] = piece
    board[sr][sc] = '.'

    turn = 'black' if turn == 'white' else 'white'
