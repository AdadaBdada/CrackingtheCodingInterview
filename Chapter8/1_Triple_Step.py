def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)


def countWays_memo(n, memo):

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = countWays_memo(n-1, memo) + countWays_memo(n-2, memo) + countWays_memo(n-3, memo)
    return memo[n]


if __name__ == "__main__":

    a = countWays(3)
    b = countWays_memo(3, memo={})
    print(b)
