import pandas as pd
import numpy as np


def analyze_bdhi_responses(responses_data):
    """
    Анализирует ответы на опросник Басса-Дарки (BDHI)

    Args:
        responses_data: список строк с ответами "Да"/"Нет" для каждого испытуемого

    Returns:
        DataFrame с результатами по всем шкалам и индексам
    """

    # Определение номеров пунктов для каждой шкалы (нумерация с 1)
    scales = {
        'physical_aggression': [1, 9, 17, 25, 33, 41, 48, 55, 62, 68],  # Физическая агрессия
        'indirect_aggression': [2, 10, 18, 26, 34, 42, 49, 56, 63],  # Косвенная агрессия
        'irritability': [3, 11, 19, 27, 35, 43, 50, 57, 64, 69, 72],  # Раздражительность
        'negativism': [4, 12, 20, 23, 36],  # Негативизм
        'resentment': [5, 13, 21, 29, 37, 44, 51, 58],  # Обида
        'suspicion': [6, 14, 22, 30, 38, 45, 52, 59, 65, 70],  # Подозрительность
        'verbal_aggression': [7, 15, 23, 31, 39, 46, 53, 60, 71, 73, 74, 75],  # Вербальная агрессия
        'guilt': [8, 16, 24, 32, 40, 47, 54, 61, 67]  # Чувство вины
    }

    # Обратные пункты (при ответе "Нет" начисляется балл)
    reverse_items = [9, 10, 11, 17, 26, 35, 39, 41, 44, 49, 65, 69, 70, 74, 75]

    results = []

    for i, response_row in enumerate(responses_data):
        # Преобразуем строку ответов в список
        if isinstance(response_row, str):
            responses = response_row.split('\t')
        else:
            responses = response_row

        # Убираем лишние пробелы
        responses = [r.strip() for r in responses]

        # Проверяем количество ответов
        if len(responses) != 75:
            print(f"Предупреждение: У испытуемого {i + 1} количество ответов {len(responses)}, ожидается 75")
            continue

        # Кодируем ответы в числа
        coded_responses = []
        for j, response in enumerate(responses):
            item_number = j + 1
            if response == "Да":
                if item_number in reverse_items:
                    coded_responses.append(0)  # Обратный пункт: Да = 0
                else:
                    coded_responses.append(1)  # Прямой пункт: Да = 1
            elif response == "Нет":
                if item_number in reverse_items:
                    coded_responses.append(1)  # Обратный пункт: Нет = 1
                else:
                    coded_responses.append(0)  # Прямой пункт: Нет = 0
            else:
                coded_responses.append(0)  # Неопределенный ответ = 0

        # Подсчет баллов по шкалам
        scale_scores = {}
        for scale_name, items in scales.items():
            score = sum(coded_responses[item - 1] for item in items if item <= len(coded_responses))
            scale_scores[scale_name] = score

        # Расчет индексов
        aggression_index = (scale_scores['physical_aggression'] +
                            scale_scores['indirect_aggression'] +
                            scale_scores['verbal_aggression'])

        hostility_index = (scale_scores['resentment'] +
                           scale_scores['suspicion'])

        total_score = sum(scale_scores.values())

        # Сохранение результатов
        result = {
            'Испытуемый': i + 1,
            'Физическая_агрессия': scale_scores['physical_aggression'],
            'Косвенная_агрессия': scale_scores['indirect_aggression'],
            'Раздражительность': scale_scores['irritability'],
            'Негативизм': scale_scores['negativism'],
            'Обида': scale_scores['resentment'],
            'Подозрительность': scale_scores['suspicion'],
            'Вербальная_агрессия': scale_scores['verbal_aggression'],
            'Чувство_вины': scale_scores['guilt'],
            'Индекс_агрессивности': aggression_index,
            'Индекс_враждебности': hostility_index,
            'Общий_балл': total_score
        }
        results.append(result)

    return pd.DataFrame(results)


# Пример использования с вашими данными
def read_responses_from_txt(file_path):
    """
    Reads responses from a txt file line by line.
    Each line should contain answers separated by tabs.

    Args:
        file_path (str): Path to the txt file.

    Returns:
        list of str: List where each element is a string of tab-separated answers.
    """
    responses = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove trailing newline and extra spaces
            clean_line = line.strip()
            if clean_line:  # Skip empty lines
                responses.append(clean_line)
    return responses


# Example usage:
file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/text.txt'  # Путь к вашему файлу с ответами
responses_data = read_responses_from_txt(file_path)
# Анализ данных
results_df = analyze_bdhi_responses(responses_data)

# Вывод результатов
print("Результаты анализа опросника Басса-Дарки:")
print("=" * 80)
print(results_df.to_string(index=False))

# Сохранение в Excel
results_df.to_excel('bdhi_results.xlsx', index=False, sheet_name='Результаты_BDHI')
print("\nРезультаты сохранены в файл 'bdhi_results.xlsx'")

# Дополнительная статистика
print("\nОписательная статистика:")
print(results_df.describe().round(2))
