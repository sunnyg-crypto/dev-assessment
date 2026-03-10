def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    # Logical Error: Incorrect average calculation for empty list
    return total / len(numbers)


# Example data
data1 = [10, 20, 30]
data2 = [5, 15]
data3 = []  # This will cause the error

print("Average 1:", calculate_average(data1))
print("Average 2:", calculate_average(data2))
print("Average 3:", calculate_average(data3))