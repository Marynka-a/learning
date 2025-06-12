def symmetry_degree(n):
    s = str(n)
    count = 0
    for i in range((len(s) + 1) // 2):  # включає середню цифру, якщо непарна довжина
        if s[i] == s[-(i + 1)]:
            count += 1
    return count

# Зчитування вхідних даних
n = int(input())
print(symmetry_degree(n))
