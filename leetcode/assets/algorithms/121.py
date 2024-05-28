"""
121. Best Time to Buy and Sell Stock
"""


def get_max_prof(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the current profit
        current_profit = price - min_price
        # Update the maximum profit if current profit is higher
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(get_max_prof(prices))