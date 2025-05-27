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

    # Поиск слов, не входящих в категории
    invalid_words = [word for word in answers if word not in categories]
    invalid_count = len(invalid_words)
    invalid_words_str = ', '.join(sorted(set(invalid_words))) if invalid_words else ''

    return count_total, count_by_category, invalid_count, invalid_words_str


# Чтение файла
filename = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/text.txt'
with open(filename, 'r', encoding='utf-8') as file:
    respondents = [line.strip() for line in file if line.strip()]

data_for_excel = []
for i, respondent in enumerate(respondents, 1):
    responses = respondent.split('\t')
    total, categories_count, invalid_count, invalid_words_str = analyze_responses(responses)

    # Подсчёт процентного соотношения для каждой категории
    # Если total = 0 (чтобы избежать деления на 0), ставим 0.0%
    percent_by_category = {
        f'{cat} (%)': (categories_count[cat] / total * 100 if total > 0 else 0.0)
        for cat in categories
    }

    # Вычисление обобщённых коэффициентов по формулам
    # Для удобства используем get с 0 по умолчанию, если категории нет в списке
    Agg = categories_count.get('Agg', 0)
    Dir = categories_count.get('Dir', 0)
    F = categories_count.get('F', 0)
    Aff = categories_count.get('Aff', 0)
    Com = categories_count.get('Com', 0)
    Dep = categories_count.get('Dep', 0)
    Exb = categories_count.get('Exb', 0)
    Crip = categories_count.get('Crip', 0)
    Act = categories_count.get('Act', 0)
    Pas = categories_count.get('Pas', 0)
    Des = categories_count.get('Des', 0)
    Ten = categories_count.get('Ten', 0)
    Bas = categories_count.get('Bas', 0)
    Fail = categories_count.get('Fail', 0)


    Integrate = (Agg + Dir) - (Aff + Com + Dep)
    Maladaptation = Ten + Crip + F
    Withdrawal = Des + Bas + Fail
    Pathology = Maladaptation + 2 * Withdrawal

    # Формируем словарь для строки Excel
    row_dict = {
        'Респондент': i,
        'Всего ответов': total,
        **categories_count,  # фактические баллы по категориям
        **percent_by_category,  # процентное соотношение по категориям
        'Ошибочные слова (кол-во)': invalid_count,
        'Ошибочные слова (список)': invalid_words_str,
        # Обобщённые коэффициенты
        'Integrate (обобщённый коэффициент)': Integrate,
        'Maladaptation (обобщённый коэффициент)': Maladaptation,
        'Withdrawal (обобщённый коэффициент)': Withdrawal,
        'Pathology (обобщённый коэффициент)': Pathology
    }
    data_for_excel.append(row_dict)

# Создаем DataFrame и сохраняем в Excel
df = pd.DataFrame(data_for_excel)
excel_filename = 'results.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Файл {excel_filename} успешно создан!")
