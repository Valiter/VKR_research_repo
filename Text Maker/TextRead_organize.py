# Файл с исходными строками
input_file = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/file1.txt'   # замените на путь к вашему файлу
output_file = 'output_categorized.txt'  # файл для сохранения результатов

# Определяем категории и ключевые слова для поиска
categories_keywords = {
    "манипуляция": ["манипуляц", "хитрость", "манипуляция", "манипулятивн"],
    "сотрудничество": ["сотрудничество"],
    "взаимовыручка": ["взаимовыручка"],
    "взаимопомощь": ["взаимопомощь"],
    "помощь": ["помощь"],
    "коммуникация": ["коммуникация"],
    "просто рассказ": ["просто рассказ"],
    "подвиг": ["подвиг"],
    "нет сказки": ["нет сказки"],
}

def categorize_line(line):
    line_clean = line.lower().strip()
    found_categories = set()

    for category, keywords in categories_keywords.items():
        for kw in keywords:
            if kw in line_clean:
                found_categories.add(category)
                break

    if not found_categories:
        found_categories.add("неопределено")

    return list(found_categories)

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue  # пропускаем пустые строки
            categories = categorize_line(line)
            categories_str = ', '.join(categories)
            # result_line = f"{i}: {line} -> Категории: {categories_str}\n"
            result_line = f"{categories_str}\n"
            print(result_line, end='')  # вывод в консоль
            outfile.write(result_line)  # запись в файл

# Запуск обработки
process_file(input_file, output_file)
