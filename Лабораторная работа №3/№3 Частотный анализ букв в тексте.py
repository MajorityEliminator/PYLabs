# TODO  Напишите функцию count_letters

def count_letters(given_text):
    letters = []
    modified_text = ""
    for char in given_text.lower():
        if char.isalpha():
            modified_text += char
            if char not in letters:
                letters += char
    amount = {}
    for char in letters:
        amount[f"{char}"] = modified_text.count(char)
    return amount
# TODO Напишите функцию calculate_frequency

def calculate_frequency(amount):
    Total_letters = 0
    for char in amount:
        Total_letters += amount[f"{char}"]
    percentage = {}
    for char in amount:
        percentage[f"{char}"] = amount[f"{char}"]/Total_letters
    return percentage



main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_percentage = calculate_frequency(count_letters(main_str))
for char in letter_percentage:
    print(f'{char}: {letter_percentage[f"{char}"]:.2f}')


# TODO Распечатайте в столбик букву и её частоту в тексте
