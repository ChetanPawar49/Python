import numpy as np

# Sample temperature data: 5 cities (rows) over 7 days (columns)
temperature_data = np.array([
    [30, 32, 33, 31, 35, 34, 36],  # City 1
    [29, 31, 34, 30, 32, 33, 31],  # City 2
    [27, 28, 29, 30, 32, 35, 33],  # City 3
    [33, 34, 36, 37, 38, 35, 34],  # City 4
    [25, 26, 27, 28, 30, 29, 31],  # City 5
])

# 1. Calculating the average temperature per city
average_temp_per_city = np.mean(temperature_data, axis=1)
print("Average Temperature per City:")
for i, avg_temp in enumerate(average_temp_per_city, start=1):
    print(f"City {i}: {avg_temp:.2f}°C")

# 2. Finding the hottest day overall and in each city
hottest_day_overall = np.max(temperature_data)
hottest_day_each_city = np.max(temperature_data, axis=1)
print("\nHottest Day Overall:", hottest_day_overall, "°C")
for i, hottest_day in enumerate(hottest_day_each_city, start=1):
    print(f"Hottest Day in City {i}: {hottest_day}°C")

# 3. Identifying the city with the highest average temperature
city_with_highest_avg_temp = np.argmax(average_temp_per_city) + 1
print("\nCity with the Highest Average Temperature: City", city_with_highest_avg_temp)

# 4. Identifying the days where the temperature in any city exceeded 35°C
days_temp_exceeded_35 = np.any(temperature_data > 35, axis=0)
days_exceeded = np.where(days_temp_exceeded_35)[0] + 1  # Adjust to 1-based day count
print("\nDays where temperature exceeded 35°C:")
print(f"Day(s): {days_exceeded}")