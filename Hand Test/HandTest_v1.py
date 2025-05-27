from collections import Counter

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

# Открываем и читаем файл
filename = '/text.txt'
with open(filename, 'r', encoding='utf-8') as file:
    respondents = [line.strip() for line in file if line.strip()]

results = []

for respondent in respondents:
    responses = respondent.split('\t')
    total, categories_count = analyze_responses(responses)
    results.append({
        'total_responses': total,
        'categories': categories_count
    })

# Вывод результатов
for i, result in enumerate(results, 1):
    print(f"Респондент {i}:")
    print(f"Всего ответов: {result['total_responses']}")
    print("Распределение по категориям:")
    for cat, count in result['categories'].items():
        if count > 0:
            print(f"  {cat}: {count}")
    print()
