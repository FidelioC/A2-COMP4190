def queens_puzzle(n) -> list[list[str]]:
    board = [["."] * n for _ in range(n)]
    queen_positions = set()
    solutions = []

    backtrack(0, n, queen_positions, board, solutions)

    return solutions


def backtrack(
    row: int,
    n: int,
    queen_positions: set[tuple[int, int]],
    board: list[list[str]],
    solutions: list[list[str]],
):
    # solution is found
    if row == n:
        solutions.append(["".join(row) for row in board])
        return

    for col in range(n):
        if is_attacked((row, col), queen_positions):
            continue

        board[row][col] = "Q"
        queen_positions.add((row, col))
        backtrack(row + 1, n, queen_positions, board, solutions)
        board[row][col] = "."
        queen_positions.remove((row, col))


def is_attacked(
    position: tuple[int, int], queen_positions: set[tuple[int, int]]
) -> bool:
    for queen in queen_positions:
        if determine_queen_attack(position, queen):
            return True
    return False


def determine_queen_attack(position_one: tuple, position_two: tuple) -> bool:
    """Determine if two queens can attack each other

    Args:
        position_one (tuple): first queen position
        position_two (tuple): second queen position
    """
    row_one, col_one = position_one
    row_two, col_two = position_two

    # row
    if row_one == row_two:
        return True

    # col
    if col_one == col_two:
        return True

    # diag
    if abs(row_one - row_two) == abs(col_one - col_two):
        return True

    return False


def main():
    input = 4
    solutions = queens_puzzle(input)
    print(solutions)


if __name__ == "__main__":
    main()
