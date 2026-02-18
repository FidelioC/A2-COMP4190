def words_from_board(board: list[list[str]], words: list[str]) -> list[str]:
    found_words = set()
    row_length = len(board)
    col_length = len(board[0])

    for word in words:
        for row in range(row_length):
            for col in range(col_length):
                if board[row][col] == word[0]:
                    visited = set()
                    if backtrack(board, word, 0, row, col, visited):
                        found_words.add(word)

    return list(found_words)


def backtrack(
    board: list[list[str]],
    word: str,
    index: int,
    row: int,
    col: int,
    visited: set[tuple[int, int]],
) -> bool:
    # check if cell is visited or cell doesn't match word index
    if (row, col) in visited or board[row][col] != word[index]:
        return False

    if index == len(word) - 1:
        return True

    visited.add((row, col))

    neighbors = FindNeighbors(row, col, len(board), len(board[0]))
    for neighbor_row, neighbor_col in neighbors:
        if backtrack(board, word, index + 1, neighbor_row, neighbor_col, visited):
            visited.remove((row, col))
            return True

    visited.remove((row, col))
    return False


def FindNeighbors(
    row: int, col: int, row_length: int, col_length: int
) -> list[tuple[int, int]]:
    """Given row and col, calculate the respective neighbors (bounded by the row and col length)

    Args:
        row (int): index row
        col (int): index column
        row_length (int): length of matrix row
        col_length (int): length of matrix column

    Returns:
        list[tuple[int, int]]: list of tuples for the respective neighbors index bounded by matrix length (row and column)
    """
    left = (0, -1)
    right = (0, 1)
    top = (-1, 0)
    bottom = (1, 0)

    neighbors_calc = [left, right, top, bottom]

    curr_cell = (row, col)
    neighbors_indices = []

    for calc in neighbors_calc:
        # calculate respective neighbors
        curr_neighbor = tuple(x + y for x, y in zip(curr_cell, calc))

        # bounds check
        neighbor_x, neighbor_y = curr_neighbor
        if 0 <= neighbor_x < row_length and 0 <= neighbor_y < col_length:
            neighbors_indices.append(curr_neighbor)

    return neighbors_indices


def main():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    solutions = words_from_board(board, words)
    print(solutions)


if __name__ == "__main__":
    main()
