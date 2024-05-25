# Функція для жадібного алгоритму
def greedy_algorithm(items, budget):
    # Сортування страв за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_cost, total_calories


# Функція для алгоритму динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            selected_items.append(item)
            w -= info['cost']

    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in selected_items)
    
    return selected_items, total_cost, total_calories


# Приклади використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
print(f"Вибрані страви: {selected_items}")
print(f"Загальна вартість: {total_cost}")
print(f"Загальна калорійність: {total_calories}")

print("\nДинамічне програмування:")
selected_items, total_cost, total_calories = dynamic_programming(items, budget)
print(f"Вибрані страви: {selected_items}")
print(f"Загальна вартість: {total_cost}")
print(f"Загальна калорійність: {total_calories}")


# Виведені результати (копія з терміналу):
# Жадібний алгоритм:
# Вибрані страви: ['cola', 'potato', 'pepsi', 'hot-dog']
# Загальна вартість: 80
# Загальна калорійність: 870

# Динамічне програмування:
# Вибрані страви: ['potato', 'cola', 'pepsi', 'pizza']
# Загальна вартість: 100
# Загальна калорійність: 970