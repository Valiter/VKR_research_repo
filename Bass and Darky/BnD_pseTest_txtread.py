def yes_no_to_binary(word):
    word = word.strip().lower()
    if word == "да":
        return 1
    elif word == "нет":
        return 0
    else:
        raise ValueError(f"Неизвестное значение: {word}")

# Читаем данные из файла
file_path = "/text.txt"  # замените на путь к вашему файлу

with open(file_path, encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

binary_rows = []
total_yes = 0
total_no = 0

for line in lines:
    words = line.split('\t')
    binary_row = []
    for word in words:
        value = yes_no_to_binary(word)
        binary_row.append(value)
        if value == 1:
            total_yes += 1
        else:
            total_no += 1
    binary_rows.append(binary_row)

# Выводим результат
for binary_row in binary_rows:
    print('\t'.join(map(str, binary_row)))

print("\nВсего 'Да':", total_yes)
print("Всего 'Нет':", total_no)
