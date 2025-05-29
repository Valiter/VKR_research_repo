import pandas as pd
import re

keywords = [
    "обман", "хитр", "манипуляц", "ковар", "лест", "подл", "интриг", "притвор", "лукав",
    "веролом", "лож", "изворотл", "расчетл", "корыст", "эгоизм", "самолюб", "тщеслав",
    "хваст", "угоднич", "льстив", "ловушк", "жадн", "использ", "влия", "управля", "одурач",
    "польст", "воспольз", "обольст", "прикидыва", "скрыт", "лицемер", "двулич", "подстав"
]


def contains_keyword(text, keywords):
    text_lower = text.lower()
    for kw in keywords:
        pattern = re.compile(r'\b' + re.escape(kw), re.IGNORECASE)
        if pattern.search(text_lower):
            return True
    return False


def process_excel_no_header(file_path, sheet_name=0, text_column_index=0):
    """
    Читает Excel без заголовков, обрабатывает текст из столбца с индексом text_column_index.

    :param file_path: путь к файлу
    :param sheet_name: лист Excel
    :param text_column_index: индекс столбца с текстом (по умолчанию 0 — первый столбец)
    :return: DataFrame с добавленным столбцом Contains_Keyword
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # Проверим, что индекс столбца корректен
    if text_column_index >= len(df.columns):
        raise IndexError(f"В файле нет столбца с индексом {text_column_index}")

    df['Contains_Keyword'] = df[text_column_index].astype(str).apply(lambda x: contains_keyword(x, keywords))

    return df


# Пример использования:
file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Story Read/Stories.xlsx'
result_df = process_excel_no_header(file_path, sheet_name=0, text_column_index=0)

# Вывести строки с найденными ключевыми словами
print(result_df[result_df['Contains_Keyword']])

# При необходимости сохранить результат
result_df.to_excel('processed_output_no_header.xlsx', index=False)
