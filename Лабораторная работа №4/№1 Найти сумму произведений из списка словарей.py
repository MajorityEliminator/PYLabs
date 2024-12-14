# TODO решите задачу
import json
def task(jsondata) -> float:
    sum = 0
    for ind in jsondata:
        sum += ind['score']*ind['weight']
    return sum

filename = 'input.json'
with open(filename) as file:
    data = json.load(file)

print(round(task(data), 4))
