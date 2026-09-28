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
    LIGHT = '\033[48;2;240;217;181m\033[38;2;0;0;0m'
    DARK = '\033[48;2;181;136;99m\033[38;2;0;0;0m'
    RESET = '\033[0m'
    
    print("\n   a  b  c  d  e  f  g  h")
    for r in range(8):
        rank = 8 - r
        line = f" {rank} "
        for c in range(8):
            bg = LIGHT if (r + c) % 2 == 0 else DARK
            icon = board[r][c]
            line += f"{bg} {icon} {RESET}"
        line += f" {rank}"
        print(line)
    print("   a  b  c  d  e  f  g  h\n")

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

def is_path_clear(sr, sc, er, ec):
    dr = 0 if sr == er else (1 if er > sr else -1)
    dc = 0 if sc == ec else (1 if ec > sc else -1)
    
    curr_r = sr + dr
    curr_c = sc + dc
    while (curr_r, curr_c) != (er, ec):
        if board[curr_r][curr_c] != '.':
            return False
        curr_r += dr
        curr_c += dc
    return True

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

def is_valid_knight_move(sr, sc, er, ec):
    dr = abs(sr - er)
    dc = abs(sc - ec)
    return (dr == 2 and dc == 1) or (dr == 1 and dc == 2)

def is_valid_rook_move(sr, sc, er, ec):
    if sr != er and sc != ec:
        return False
    return is_path_clear(sr, sc, er, ec)

def is_valid_bishop_move(sr, sc, er, ec):
    if abs(sr - er) != abs(sc - ec):
        return False
    return is_path_clear(sr, sc, er, ec)

def is_valid_queen_move(sr, sc, er, ec):
    if (sr == er or sc == ec) or (abs(sr - er) == abs(sc - ec)):
        return is_path_clear(sr, sc, er, ec)
    return False

def is_valid_king_move(sr, sc, er, ec):
    return max(abs(sr - er), abs(sc - ec)) == 1

def is_valid_move(sr, sc, er, ec, piece):
    p = piece.lower()
    if p == 'p':
        return is_valid_pawn_move(sr, sc, er, ec, piece)
    elif p == 'n':
        return is_valid_knight_move(sr, sc, er, ec)
    elif p == 'r':
        return is_valid_rook_move(sr, sc, er, ec)
    elif p == 'b':
        return is_valid_bishop_move(sr, sc, er, ec)
    elif p == 'q':
        return is_valid_queen_move(sr, sc, er, ec)
    elif p == 'k':
        return is_valid_king_move(sr, sc, er, ec)
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

    if not is_valid_move(sr, sc, er, ec, piece):
        print(f"Invalid move for {piece}!")
        continue

    board[er][ec] = piece
    board[sr][sc] = '.'

    turn = 'black' if turn == 'white' else 'white'
