memo = {0: 0, 1: 1}


def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fib(100))
