def playSegments(coins):
    n = len(coins)
    lc = [0] * n  # Left cumulative score
    rc = [0] * (n + 1)  # Right cumulative score (n+1 to avoid index error)

    # Calculate left cumulative score for Player 1
    for i in range(n):
        if coins[i] == 1:
            lc[i] = lc[i - 1] + 1
        else:
            lc[i] = lc[i - 1] - 1

    # Initialize rc[-1] to 0 (Player 2 starts at 0)
    rc[n] = 0

    # Calculate right cumulative score for Player 2
    for i in range(n-1, -1, -1):
        if coins[i] == 1:
            rc[i] = rc[i + 1] + 1
        else:
            rc[i] = rc[i + 1] - 1

    print(lc, rc)

    for i in range(len(lc)):
        if lc[i]>rc[i]:
            return i


def main():
    coins = [1,0,0,1,0]
    # sol_obj = Solution()
    result = playSegments(coins)
    print(result)


if __name__ == '__main__':
    main()
