def fibonnaci(n,memo= {}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fibonnaci(n-1,memo) + fibonnaci(n-2,memo)
    return memo[n]
print(fibonnaci(10))


def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci(10))  # Output: 55
