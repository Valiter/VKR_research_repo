import pandas as pd

def round_numbers_and_save_excel(input_file, output_file, delimiter='\t'):
    count = 0  # счётчик ошибок
    data = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            parts = line.strip().split(delimiter)
            rounded_parts = []
            for part in parts:
                part = part.strip()
                try:
                    num = float(part)
                    if not num.is_integer():
                        num = round(num, 2)
                    rounded_parts.append(num)
                except ValueError:
                    count += 1
                    print(f"ValueError {count} for value: '{part}'")
                    rounded_parts.append(part)
            data.append(rounded_parts)

    # Создаём DataFrame из списка списков
    df = pd.DataFrame(data)

    # Сохраняем в Excel
    df.to_excel(output_file, index=False, header=False)
    print(f"Файл сохранён: {output_file}")

# Пример использования:
input_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/numbers.txt'
output_path = 'output.xlsx'
round_numbers_and_save_excel(input_path, output_path)
