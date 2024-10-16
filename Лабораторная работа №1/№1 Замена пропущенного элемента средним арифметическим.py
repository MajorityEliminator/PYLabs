numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

Noneid = numbers.index(None)
numbers_without_none = numbers[0:Noneid] + numbers[Noneid+1:]
sum_ = sum(numbers_without_none)
avg = sum_/len(numbers)
numbers[Noneid] = avg

print(f"Измененный список:", numbers)
