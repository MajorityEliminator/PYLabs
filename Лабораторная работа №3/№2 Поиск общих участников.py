# TODO Напишите функцию find_common_participants

def find_common_participants(participant_list_1, participant_list_2, splitarg=","):
    similarities = list(set(participant_list_1.split(splitarg)).intersection(participant_list_2.split(splitarg)))
    similarities.sort()
    return similarities


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой


print(f"Список общих участников групп: {find_common_participants(participants_first_group, participants_second_group, '|')}")
