from collections import Counter
import pandas as pd

# Список категорий для анализа
categories = ['Agg', 'Dir', 'F', 'Aff', 'Com', 'Dep', 'Exb', 'Crip',
              'Act', 'Pas', 'Des', 'Ten', 'Bas', 'Fail']


def analyze_responses(responses):
    answers = []
    for part in responses:
        subparts = part.split(',')
        for sp in subparts:
            answers.extend([x.strip() for x in sp.split() if x.strip()])
    count_total = len(answers)
    counter = Counter(answers)
    count_by_category = {cat: counter.get(cat, 0) for cat in categories}
    return count_total, count_by_category


# Чтение файла
filename = '/text.txt'
with open(filename, 'r', encoding='utf-8') as file:
    respondents = [line.strip() for line in file if line.strip()]

# Обработка данных
data_for_excel = []
for i, respondent in enumerate(respondents, 1):
    responses = respondent.split('\t')
    total, categories_count = analyze_responses(responses)

    # Формируем строку для Excel
    row_dict = {
        'Респондент': i,
        'Всего ответов': total,
        **categories_count  # Распаковываем счетчики категорий
    }
    data_for_excel.append(row_dict)

# Создаем DataFrame и сохраняем в Excel
df = pd.DataFrame(data_for_excel)
excel_filename = '../results.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Файл {excel_filename} успешно создан!")
