numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_numbers = sum([x for x in numbers if x is not None])
count_numbers = len(numbers)

missing_index = numbers.index(None)

numbers[missing_index] = sum_numbers / count_numbers

print("Измененный список:", numbers)