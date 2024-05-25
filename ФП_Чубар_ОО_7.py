import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    # Підрахунок кількості появ кожної суми від 2 до 12
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_dices = dice1 + dice2
        counts[sum_dices] += 1

    # Обчислення ймовірностей
    probabilities = {k: v / num_trials for k, v in counts.items()}
    return probabilities

def plot_probabilities(probabilities, analytical_probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    analytical_probs = [analytical_probabilities[s] for s in sums]
    
    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, alpha=0.5, label='Монте-Карло', color='blue')
    plt.plot(sums, analytical_probs, marker='o', color='red', label='Аналітичні')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум на кубиках: Монте-Карло vs Аналітичні')
    plt.legend()
    plt.grid(True)
    plt.show()

# Виконання симуляції
num_trials = 100000
probabilities = monte_carlo_simulation(num_trials)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Виведення результатів симуляції
print("Результати симуляції Монте-Карло:")
for sum_value, prob in probabilities.items():
    print(f"Сума {sum_value}: {prob:.4%}")

print("\nАналітичні значення:")
for sum_value, prob in analytical_probabilities.items():
    print(f"Сума {sum_value}: {prob:.4%}")

# Побудова графіка
plot_probabilities(probabilities, analytical_probabilities)
