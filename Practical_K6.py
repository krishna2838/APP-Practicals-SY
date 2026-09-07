def knapsack(weights,profit,capacity):
    n=len(weights)
    dp=[[0]*(capacity + 1)for i in range(n + 1)]
    for i in range(1,n+1):
        for w in range(capacity + 1):
            if weights[i-1]>w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    profit = int(input(f"Enter profit of item {i + 1}: "))
    weights.append(weight)
    profits.append(profit)

capacity = int(input("Enter knapsack capacity: "))

max_profit, items = knapsack(weights, profits, capacity)

print("Maximum Profit:", max_profit)
print("Items in Knapsack:", items)