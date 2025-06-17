def find_pirates(a, m):
    for n in range(2, 1000):  # n > 1, межа підібрана з запасом
        sum_without_captain = ((2 * a + (n - 2)) * (n - 1)) // 2
        captain_share = 2 * (a + n - 1)
        total = sum_without_captain + captain_share
        if total == m:
            return n
    return -1  # якщо не знайдено

# Зчитування вхідних даних
a, m = map(int, input().split())

# Вивід результату
print(find_pirates(a, m))
