def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def max_visits(intervals):
    # Перетворюємо час у хвилини
    converted = [(time_to_minutes(start), time_to_minutes(end)) for start, end in intervals]
    
    # Сортуємо за часом закінчення
    converted.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for start, end in converted:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

# Зчитування даних
n = int(input())
intervals = [tuple(input().split()) for _ in range(n)]

# Виведення результату
print(max_visits(intervals))
