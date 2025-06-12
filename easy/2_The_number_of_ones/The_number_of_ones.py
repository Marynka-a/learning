def min_ones(n):
    dp = [float('inf')] * (n + 1)
    dp[1] = 1  # Єдина одиниця для числа 1

    for i in range(2, n + 1):
        # Перевіряємо варіант побудови через додавання
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])

        # Перевіряємо варіант побудови через множення
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + dp[i // j])

    return dp[n]

# Зчитуємо вхідне число
n = int(input())
print(min_ones(n))
