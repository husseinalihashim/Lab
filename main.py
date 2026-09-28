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

while True:
    show_board()
    move = input("Move: ").strip().lower()
    
    if move in ['quit', 'exit']:
        break
        
    if len(move) != 4:
        print("Invalid format. Use 4 chars like e2e4.")
        continue
        
    src = parse_pos(move[:2])
    dst = parse_pos(move[2:])
    
    if not src or not dst:
        print("Invalid coordinates. Stay inside a1-h8.")
        continue
        
    r1, c1 = src
    r2, c2 = dst
    
    if board[r1][c1] == '.':
        print("No piece at source square.")
        continue
        
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = '.'
