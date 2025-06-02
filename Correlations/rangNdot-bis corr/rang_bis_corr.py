

import os
from itertools import count
import openpyxl

"""Сортировка пузырьком ->
потом расстановка рангов ->
потом присвоение ранга в изначальный список значений ->
потом подсчет согласно рангово-бисериальному коэффициенту корреляции
"""


#
def bubble_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    for i in range(n):
        # Проходим по массиву, уменьшая количество проверяемых элементов с каждым проходом
        for j in range(0, n - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                # Меняем элементы местами, если они идут в неправильном порядке
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]

def analyze_txt_files(folder_path):
    results = {}
    names_in_dir = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.txt'):  # фильтрация по расширению .txt
                file_path = os.path.join(root, file)
                lines_count = 0
                words_count = 0
                symbols_count = 0
                content = []  # список для хранения строк файла
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            content.append(line.rstrip('\n'))  # сохраняем строку без символа переноса строки
                            lines_count += 1
                            words_count += len(line.split())
                            symbols_count += len(line)
                    names_in_dir.append(file_path)
                    results[file_path] = {
                        'lines': lines_count,
                        'words': words_count,
                        'symbols': symbols_count,
                        'content': content
                    }
                except (UnicodeDecodeError, OSError) as e:
                    results[file_path] = f"Ошибка чтения файла: {e}"
    return results, names_in_dir


def calculate_ranks(sorted_list):
    """
    Вычисляет ранги для отсортированного списка с учётом связанных значений.
    """
    ranks = [0.0] * len(sorted_list)
    n = len(sorted_list)
    i = 0

    while i < n:
        j = i + 1
        while j < n and sorted_list[j] == sorted_list[i]:
            j += 1
        avg_rank = (i + 1 + j) / 2
        for k in range(i, j):
            ranks[k] = avg_rank
        i = j

    return ranks


def assign_ranks(not_sorted_data):
    """
    Сортирует список пузырьком, вычисляет ранги и возвращает исходные элементы с рангами.
    """
    # Создаём копию для сортировки, сохраняя исходные индексы
    indexed_data = list(enumerate(not_sorted_data))
    n = len(indexed_data)

    # Сортировка пузырьком по значениям (с сохранением исходных индексов)
    for i in range(n):
        for j in range(0, n - i - 1):
            if indexed_data[j][1] > indexed_data[j + 1][1]:
                indexed_data[j], indexed_data[j + 1] = indexed_data[j + 1], indexed_data[j]

    # Вычисляем ранги для отсортированного списка
    sorted_values = [item[1] for item in indexed_data]
    ranks = calculate_ranks(sorted_values)

    # Создаём словарь: исходный индекс -> ранг
    rank_dict = {indexed_data[i][0]: ranks[i] for i in range(n)}

    # Формируем результат в исходном порядке
    return [[num, rank_dict[i]] for i, num in enumerate(not_sorted_data)], sorted_values, ranks


def rank_biserial_correlation(y_binary, x_values):

    #print(set(y_binary))
    #print(len(y_binary), len(x_values))

    y_binary = [int(val) for val in y_binary]

    print(set(y_binary))
    print(len(y_binary), len(x_values))

    """
    Вычисляет рангово-бисеральный коэффициент корреляции по формуле:
    r = 2/n * (mean_rank_1 - mean_rank_0)

    Параметры:
        y_binary: список из 0 и 1 (бинарная переменная)
        x_values: список числовых значений

    Возвращает:
        float: коэффициент рангово-бисеральной корреляции
    """
    n = len(y_binary)
    ranks = x_values

    # Собираем ранги по группам
    ranks_1 = [r for r, y in zip(ranks, y_binary) if y == 1]
    ranks_0 = [r for r, y in zip(ranks, y_binary) if y == 0]

    mean_rank_1 = sum(ranks_1) / len(ranks_1) if ranks_1 else 0
    mean_rank_0 = sum(ranks_0) / len(ranks_0) if ranks_0 else 0

    r = (2 / n) * (mean_rank_1 - mean_rank_0)

    print(f"Средний ранг для группы 1: {mean_rank_1}")
    print(f"Средний ранг для группы 0: {mean_rank_0}")
    print(f"Общий размер выборки: {n}")

    return r

def biserial_file_reading():
    """
    Читает текстовый файл и возвращает список строк.

    Parameters:
        filename (str): путь к текстовому файлу

    Returns:
        list: список строк из файла без символов перевода строки
    """
    bis_name = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/rangNdot-bis corr/variable_of_story_point.txt'
    data = []
    with open(bis_name, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())  # убираем символы перевода строки и пробелы
    return data

def save_single_correlation_to_excel(key, r_rb, output_filename):
    """
    Сохраняет одну пару (ключ, коэффициент корреляции) в Excel файл.
    Если файл не существует — создаёт и добавляет заголовок.
    Если файл есть — дописывает данные в конец.

    Параметры:
        key (str): название или идентификатор
        r_rb (float): коэффициент корреляции
        output_filename (str): путь и имя Excel файла

    Возвращает:
        None
    """
    to_remove = "/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/rangNdot-bis corr/variables_directory"
    new_path = key.replace(to_remove, "")
    print(new_path)
    if not output_filename.lower().endswith('.xlsx'):
        output_filename += '.xlsx'

    if os.path.exists(output_filename):
        wb = openpyxl.load_workbook(output_filename)
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Correlation Results"
        ws.append(["Ключ", "Коэффициент корреляции"])  # заголовок

    ws.append([new_path, f"{r_rb:.4f}"])
    wb.save(output_filename)


"""Рабочее тело, где мы все вызываем и работаем"""


text_variables_in_directory, txt_file_names = analyze_txt_files('/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/rangNdot-bis corr/variables_directory')
print(text_variables_in_directory)

for count, el in enumerate(txt_file_names, start=1):
    print(f'Папка номер {count}: {el}')

print("\n")

for key in txt_file_names:
    if key in text_variables_in_directory:
        content = text_variables_in_directory[key].get('content', None)
        ranks_as_is = []
        data_as_is = []
        result, data, ranks = assign_ranks(content)

        for item in result:
            ranks_as_is.append(item[1])
            data_as_is.append(item[0])

        print("Данные отсортированные: ", data)
        print("Список рангов по порядку:", ranks)
        print("Данные сырые: ", data_as_is)
        print("Список как сырые:", ranks_as_is)
        print(f'Бисериальные данные {biserial_file_reading()}')

        r_rb = rank_biserial_correlation(biserial_file_reading(), ranks_as_is)
        print(f"Рангово-бисеральный коэффициент корреляции: {r_rb:.4f}")
        #print("Исходные данные с рангами:")
        #for item in result:
        #    print(f"{item[0]} -> {item[1]:.1f}")
        save_single_correlation_to_excel(key, r_rb, "ИтоговаяТаблицаEXCEL")


        if content is not None:
            print(f"Ключ: {key}, Content: {content}\n")
        else:
            print(f"Ключ: {key} найден, но 'content' отсутствует")
    else:
        print(f"Ключ: {key} отсутствует во внешнем словаре")


