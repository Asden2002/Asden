import json

INPUT_FILENAME = "input.json"


def task() -> float:
    # Чтение данных из JSON файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)  # Загружаем JSON как список словарей

    # Вычисление суммы произведений
    total = sum(d['score'] * d['weight'] for d in data)

    # Возвращаем результат, округленный до 3 знаков после запятой
    return round(total, 3)


print(task())