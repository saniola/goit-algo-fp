def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_items = []
    remaining_budget = budget

    for item_name, item_data in sorted_items:
        if item_data["cost"] <= remaining_budget:
            selected_items.append(item_name)
            remaining_budget -= item_data["cost"]

    return selected_items


def dynamic_programming(items, budget):
    num_items = len(items)
    calc_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i, (item_name, item_data) in enumerate(items.items(), start=1):
        cost, calories = item_data["cost"], item_data["calories"]

        for j in range(budget + 1):
            if cost <= j:
                calc_table[i][j] = max(
                    calc_table[i - 1][j], calc_table[i - 1][j - cost] + calories
                )
            else:
                calc_table[i][j] = calc_table[i - 1][j]

    selected_items = []
    i, j = num_items, budget
    while i > 0 and j > 0:
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]["cost"]

        if calc_table[i][j] != calc_table[i - 1][j]:
            selected_items.append(item_name)
            j -= cost

        i -= 1

    return selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy algorithm result:", greedy_result)
print("Dynamic programming result:", dp_result)
