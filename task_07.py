import random
import matplotlib.pyplot as plt


def throw_dice():
    return random.randint(1, 6)


def simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        roll1 = throw_dice()
        roll2 = throw_dice()
        total = roll1 + roll2
        results[total] += 1

    probabilities = {key: value / num_simulations for key, value in results.items()}
    return probabilities


def plot_probabilities(probabilities, math_probabilities, name):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())
    math_values = list(math_probabilities.values())

    plt.bar(sums, probabilities_values, color="blue", alpha=0.5, label="Simulation")
    plt.bar(
        sums,
        math_values,
        color="red",
        alpha=0.5,
        align="edge",
        width=0.5,
        label="Mathematics",
    )
    plt.legend()
    plt.xlabel("Sum per Simulation")
    plt.ylabel("Probability")
    plt.title(name)
    plt.xticks(sums)
    plt.show()


num_simulations = 50000
probabilities = simulation(num_simulations)
math_probabilities = {
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278,
}
plot_probabilities(probabilities, math_probabilities, "Monte Carlo Simulation 50,000")
