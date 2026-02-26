def dp_pile_stones_game(piles: list) -> bool:
    """dp bottom up approach"""
    n = len(piles)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = piles[i]

    # start from beginning pile to last pile
    for length in range(2, n + 1):
        for i in range(n - length + 1):  # i = for the left pile
            j = i + length - 1  # j = for the right pile
            dp[i][j] = max(
                piles[i] - dp[i + 1][j],  # take the left pile
                piles[j] - dp[i][j - 1],  # take the right pile
            )

    return dp[0][n - 1] > 0  # if Alice's pile is positive, then she wins


def main():
    piles: list = [3, 7, 2, 3]
    solution = dp_pile_stones_game(piles)
    print(solution)


if __name__ == "__main__":
    main()
