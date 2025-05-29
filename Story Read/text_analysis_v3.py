import pandas as pd
import re

keywords = [
    "обман", "хитр", "манипуляц", "ковар", "лест", "подл", "интриг", "притвор", "лукав",
    "веролом", "лож", "изворотл", "расчетл", "корыст", "эгоизм", "самолюб", "тщеслав",
    "хваст", "угоднич", "льстив", "ловушк", "жадн", "использ", "влия", "управля", "одурач",
    "польст", "воспольз", "обольст", "прикидыва", "скрыт", "лицемер", "двулич", "подстав"
]


def count_keyword_occurrences(text, keywords):
    """
    Считает количество вхождений каждого корня из keywords в тексте.
    Возвращает словарь {корень: количество}
    """
    text_lower = text.lower()
    counts = {}
    for kw in keywords:
        # Ищем все вхождения корня слова (начало слова)
        pattern = re.compile(r'\b' + re.escape(kw), re.IGNORECASE)
        matches = pattern.findall(text_lower)
        counts[kw] = len(matches)
    return counts


def process_excel_with_counts(file_path, sheet_name=0, text_column_index=0):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    if text_column_index >= len(df.columns):
        raise IndexError(f"В файле нет столбца с индексом {text_column_index}")

    # Функция для одной ячейки: возвращает словарь с подсчетом
    def analyze_text(text):
        counts = count_keyword_occurrences(str(text), keywords)
        total = sum(counts.values())
        contains = total > 0
        return contains, total, counts

    # Применяем к столбцу с текстом
    results = df[text_column_index].apply(analyze_text)

    # Распаковываем результаты в отдельные столбцы
    df['Contains_Keyword'] = results.apply(lambda x: x[0])
    df['Total_Matches'] = results.apply(lambda x: x[1])

    # Создаем столбцы для каждого ключевого корня
    for kw in keywords:
        df[f'Count_{kw}'] = results.apply(lambda x: x[2].get(kw, 0))

    return df


# Пример использования:
file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Story Read/Stories.xlsx'
result_df = process_excel_with_counts(file_path, sheet_name=0, text_column_index=0)

# Выводим строки, где есть хотя бы одно ключевое слово, с подсчетами
print(result_df[result_df['Contains_Keyword']])

# При необходимости сохранить результат в Excel
result_df.to_excel('processed_with_counts.xlsx', index=False)
