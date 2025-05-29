# Файл с исходными строками
input_file = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/file1.txt'   # замените на путь к вашему файлу
output_file = 'output_categorized.txt'  # файл для сохранения результатов

# Определяем категории и ключевые слова для поиска
categories_keywords = {
    "манипуляция": ["манипуляц", "хитрость", "манипулятивн"],
    "сотрудничество": ["сотрудничество"],
    "взаимовыручка": ["взаимовыручка"],
    "взаимопомощь": ["взаимопомощь"],
    "помощь": ["помощь"],
    "коммуникация": ["коммуникация"],
    "просто рассказ": ["просто рассказ"],
    "подвиг": ["подвиг"],
    "нет сказки": ["нет сказки"],
}

def categorize_line_with_counts(line):
    line_clean = line.lower().strip()
    category_counts = {}

    for category, keywords in categories_keywords.items():
        count = 0
        for kw in keywords:
            count += line_clean.count(kw)
        if count > 0:
            category_counts[category] = count

    if not category_counts:
        category_counts["неопределено"] = 0

    return category_counts

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue  # пропускаем пустые строки
            categories = categorize_line_with_counts(line)
            categories_str = ', '.join(categories)
            # result_line = f"{i}: {line} -> Категории: {categories_str}\n"
            result_line = ' '.join(f"{word} {count}" for word, count in categories.items()) + '\n'
            print(result_line, end='')  # вывод в консоль
            outfile.write(result_line)  # запись в файл

# Запуск обработки
process_file(input_file, output_file)
