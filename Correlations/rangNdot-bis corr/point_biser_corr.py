import os
from scipy.stats import pointbiserialr
import openpyxl

def biserial_file_reading():
    """
    Читает бинарную переменную из файла и возвращает список чисел 0/1.
    """
    bis_name = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/rangNdot-bis corr/variable_of_story_point.txt'
    data = []
    with open(bis_name, 'r', encoding='utf-8') as file:
        for line in file:
            value = line.strip()
            if value in ('0', '1'):
                data.append(int(value))
            else:
                # Если данные не бинарные, можно обработать ошибку или пропустить
                raise ValueError(f"Неверное значение бинарной переменной: {value}")
    return data


def analyze_txt_files(folder_path):
    """
    Читает все .txt файлы из папки, возвращает словарь с метаданными и содержимым.
    """
    results = {}
    names_in_dir = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                lines_count = 0
                words_count = 0
                symbols_count = 0
                content = []
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            content.append(line.rstrip('\n'))
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


def convert_content_to_float_list(content):
    """
    Преобразует список строк с числами в список float.
    Предполагается, что каждая строка — одно число.
    """
    float_list = []
    for line in content:
        try:
            float_list.append(float(line))
        except ValueError:
            # Можно обработать или пропустить строки с ошибками
            print(f"Warning: невозможно преобразовать '{line}' в число.")
    return float_list



def save_single_correlation_to_excel(key, r_rb, p_value, output_filename):
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
        ws.append(["Ключ", "Коэффициент корреляции", "P-value"])  # заголовок

    ws.append([new_path, f"{r_rb:.4f}", f"{p_value:.4e}"])
    wb.save(output_filename)


# Основной блок
if __name__ == "__main__":
    # Читаем бинарную переменную
    x = biserial_file_reading()

    # Путь к директории с файлами непрерывных переменных
    folder_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/rangNdot-bis corr/variables_directory'

    # Читаем все txt-файлы из папки
    text_variables_in_directory, txt_file_names = analyze_txt_files(folder_path)

    # Для каждого файла считаем корреляцию с бинарной переменной x
    for file_path in txt_file_names:
        file_data = text_variables_in_directory.get(file_path, None)
        if file_data is None or isinstance(file_data, str):
            print(f"Не удалось прочитать файл {file_path}: {file_data}")
            continue

        content = file_data.get('content', None)
        if content is None:
            print(f"В файле {file_path} отсутствует содержимое.")
            continue

        # Преобразуем содержимое файла в список чисел
        y = convert_content_to_float_list(content)

        # Проверка на пустой список
        if not y:
            print(f"Файл {file_path} пустой или не содержит числовых данных. Пропускаем.")
            continue

        # Проверяем, что длины x и y совпадают
        if len(x) != len(y):
            print(f"Длина бинарной переменной ({len(x)}) и переменной из файла {file_path} ({len(y)}) не совпадают. Пропускаем.")
            continue

        # Вычисляем точечно-бисериальную корреляцию
        correlation_coefficient, p_value = pointbiserialr(x, y)

        print(f"Файл: {file_path}")
        print(f"Точечно-бисериальный коэффициент корреляции: {correlation_coefficient:.4f}")
        print(f"P-значение: {p_value:.4e}")
        print('-' * 40)

        save_single_correlation_to_excel(file_path, correlation_coefficient, p_value, "ИтоговаяТаблицаEXCEL_точечноБисериальный")
