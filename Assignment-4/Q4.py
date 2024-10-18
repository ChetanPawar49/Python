import numpy as np

# Sample stock prices: 4 stocks (rows) over 10 days (columns)
stock_prices = np.array([
    [150, 152, 148, 145, 149, 155, 160, 162, 158, 159],  # Stock 1
    [210, 201, 215, 220, 218, 225, 230, 233, 231, 228],  # Stock 2
    [120, 121, 122, 125, 127, 130, 128, 126, 125, 123],  # Stock 3
    [90, 92, 95, 93, 96, 100, 98, 99, 101, 103],         # Stock 4
])

# 1. Calculate the daily percentage change for each stock
daily_pct_change = np.diff(stock_prices) / stock_prices[:, :-1] * 100
print("Daily Percentage Change for Each Stock (%):")
print(daily_pct_change)

# 2. Identify the stock with the highest volatility (largest variance in daily returns)
volatility = np.var(daily_pct_change, axis=1)
stock_with_highest_volatility = np.argmax(volatility) + 1
print(f"\nStock with the Highest Volatility: Stock {stock_with_highest_volatility}")

# 3. Determine the best-performing stock over the 10-day period (based on total percentage gain)
total_pct_change = (stock_prices[:, -1] - stock_prices[:, 0]) / stock_prices[:, 0] * 100
best_performing_stock = np.argmax(total_pct_change) + 1
print(f"\nBest Performing Stock Over 10 Days: Stock {best_performing_stock}")

# 4. Find the days where any stock price dropped more than 5% from the previous day
drops_more_than_5_percent = daily_pct_change < -5
days_with_drops = np.where(drops_more_than_5_percent)
print("\nDays where any stock dropped more than 5% from the previous day:")
for stock_idx, day_idx in zip(days_with_drops[0], days_with_drops[1]):
    print(f"Stock {stock_idx + 1} on Day {day_idx + 2}")  # Adjust day to 1-based index