numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

Noneid = numbers.index(None)

avg = (sum(numbers[0:Noneid]) + sum(numbers[Noneid+1:]))/len(numbers)
numbers[Noneid] = avg

print(f"Измененный список:", numbers)
