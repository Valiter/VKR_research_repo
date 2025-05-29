import pandas as pd
import re
import string

keywords = [
    # Ваш исходный список корней слов
    "обман", "хитр", "манипуляц", "ковар", "лест", "подл", "интриг", "притвор", "лукав",
    "веролом", "лож", "изворотл", "расчетл", "корыст", "эгоизм", "самолюб", "тщеслав",
    "хваст", "угоднич", "льстив", "ловушк", "жадн", "использ", "влия", "управля", "одурач",
    "польст", "воспольз", "обольст", "прикидыва", "скрыт", "лицемер", "двулич", "подстав", "жал",
    # Добавленные корни и вариации
    "коварств", "вероломств", "манипуляц", "цинизм", "подкуп", "подлог", "мошеннич",
    "лицемер", "плутовств", "лукавств", "эксплуатац", "интриг", "подлост", "предательств",
    "злокозн", "злонамерен", "жёстк", "игнорир", "эмоциональн", "притворств", "ложь",
    "воровств", "подделк", "ухищр", "афер", "махинац", "сговор", "уловк", "шантаж",
    "провокац", "искажен", "злоупотреблен", "измен", "козн", "врань", "шарлатанств",
    "коррупц", "влияни", "воздейств", "действ", "авторитет",
    "давлен", "эффект", "авторитетн", "значен", "вес", "престиж", "побужд", "подчинен",
    "доминир", "внушен", "власт", "инспирац", "угнетен", "притеснен", "взаимовлия"
]

phrases_patterns = [
    # Исходные варианты "желанный" и "помогу"
    r'желанн\w*(?:\W+\w+){0,5}?\W+но',
    r'помог\w*(?:\W+\w+){0,5}?\W+если',

    # Варианты из группы 1 — противопоставления
    r'желаем\w*(?:\W+\w+){0,5}?\W+однако',
    r'долгождан\w*(?:\W+\w+){0,5}?\W+но',
    r'важн\w*(?:\W+\w+){0,5}?\W+но',
    r'нужн\w*(?:\W+\w+){0,5}?\W+однако',
    r'дорог\w*(?:\W+\w+){0,5}?\W+но',
    r'интересн\w*(?:\W+\w+){0,5}?\W+но',
    r'приятн\w*(?:\W+\w+){0,5}?\W+но',

    # Варианты из группы 2 — условные конструкции
    r'сдела\w*(?:\W+\w+){0,5}?\W+если',
    r'помог\w*(?:\W+\w+){0,5}?\W+когда',
    r'поддерж\w*(?:\W+\w+){0,5}?\W+если',
    r'помогат\w*(?:\W+\w+){0,5}?\W+когда',
    r'помог\w*(?:\W+\w+){0,5}?\W+только\W+если',
    r'помог\w*(?:\W+\w+){0,5}?\W+в\W+случае\W+если',
    r'помог\w*(?:\W+\w+){0,5}?\W+при\W+условии\W+что',

    # Новые варианты на тему "отпущу тебя, если"
    r'отпущ\w*(?:\W+\w+){0,5}?\W+тебя(?:\W+\w+){0,5}?\W+если',
    r'отпуст\w*(?:\W+\w+){0,5}?\W+тебя(?:\W+\w+){0,5}?\W+если',
    r'отпущ\w*(?:\W+\w+){0,5}?\W+тебе(?:\W+\w+){0,5}?\W+если',
    r'отпуст\w*(?:\W+\w+){0,5}?\W+тебе(?:\W+\w+){0,5}?\W+если',
]

def preprocess_text(text):
    """
    Приводит текст к нижнему регистру и удаляет все знаки препинания.
    """
    text = text.lower()
    # Удаляем знаки препинания
    text = re.sub(rf"[{re.escape(string.punctuation)}]", " ", text)
    # Удаляем лишние пробелы
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def count_keyword_occurrences(text, keywords):
    """
    Считает количество вхождений каждого корня из keywords в тексте.
    Возвращает словарь {корень: количество}
    """
    text_processed = preprocess_text(text)
    counts = {}
    for kw in keywords:
        pattern = re.compile(r'\b' + re.escape(kw), re.IGNORECASE)
        matches = pattern.findall(text_processed)
        counts[kw] = len(matches)
    return counts

def search_phrases(text, patterns):
    """
    Ищет в тексте шаблоны сочетаний слов с промежуточными словами.
    Возвращает словарь {шаблон: True/False}
    """
    text_processed = preprocess_text(text)
    results = {}
    for pattern in patterns:
        regex = re.compile(pattern, re.IGNORECASE)
        results[pattern] = bool(regex.search(text_processed))
    return results

def process_excel_with_counts(file_path, sheet_name=0, text_column_index=0):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    if text_column_index >= len(df.columns):
        raise IndexError(f"В файле нет столбца с индексом {text_column_index}")

    def analyze_text(text):
        counts = count_keyword_occurrences(str(text), keywords)
        total = sum(counts.values())
        contains = total > 0

        phrases_found = search_phrases(str(text), phrases_patterns)
        contains_phrases = any(phrases_found.values())

        contains_any = contains or contains_phrases

        return contains_any, total, counts, phrases_found

    results = df[text_column_index].apply(analyze_text)

    df['Contains_Keyword_or_Phrase'] = results.apply(lambda x: x[0])
    df['Total_Matches'] = results.apply(lambda x: x[1])

    for kw in keywords:
        df[f'Count_{kw}'] = results.apply(lambda x: x[2].get(kw, 0))

    for pattern in phrases_patterns:
        col_name = pattern.replace(r'(?:\W+\w+){0,5}?', '_..._').replace(r'\W+', '_').replace(r'\\', '')
        df[f'Phrase_{col_name}'] = results.apply(lambda x: x[3].get(pattern, False))

    return df

# Пример использования:
file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Story Read/Stories.xlsx'
result_df = process_excel_with_counts(file_path, sheet_name=0, text_column_index=0)

print(result_df[result_df['Contains_Keyword_or_Phrase']])

result_df.to_excel('processed_with_counts_and_phrases.xlsx', index=False)
