# Данные для записи
data = [
    "ТТ_Макиавеллизм",
    "ТТ_Нарциссизм",
    "ТТ_Психопатия",
    "БД_Физическая_агрессия",
    "БД_Косвенная_агрессия",
    "БД_Раздражительность",
    "БД_Негативизм",
    "БД_Обида",
    "БД_Подозрительность",
    "БД_Вербальная_агрессия",
    "БД_Чувство_вины",
    "БД_Индекс_Агрессивности",
    "БД_Индекс_Враждебности",
    "БД_Общий_балл",
    "РНЖ_Сумма",
    "Всего_ответов",
    "Agg(%)",
    "Dir(%)",
    "F(%)",
    "Aff(%)",
    "Com(%)",
    "Dep (%)",
    "Exb(%)",
    "Crip(%)",
    "Act (%)",
    "Pas(%)",
    "Des(%)",
    "Ten(%)",
    "Bas(%)",
    "Fail(%)",
    "Integrate_обобщённый_коэффициент",
    "Maladaptation_обобщённый_коэффициент",
    "Withdrawal_обобщённый_коэффициент",
    "Pathology_обобщённый_коэффициент",
    "Номинальный_балл_за_сказку"
]

print(f'Число строк в исходных данных: {len(data)}')
# Имя файла


def rewriting_data(information):
    total_count = 0
    data_rewrited = []
    total = len(information)
    for first_v in range(total):
        for second_v in range(first_v + 1, total):
            data_rewrited.append(f"{information[first_v]}x{information[second_v]}")
            total_count += 1

    return data_rewrited, total_count


def writing_data_in(information, filename, total_xcx_count):
    # Открываем файл для записи ('w' - write)
    with open(filename, 'w', encoding='utf-8') as file:
        for line in information:
         file.write(line + '\n')  # Записываем строку и переводим на новую
    print(f"Файл '{filename}' успешно создан и заполнен.\n Всего пар переменных: {total_xcx_count}")

filename_global = "output_columns.txt"
data_rewrited, total_xnx = rewriting_data(data)
writing_data_in(data_rewrited, filename_global, total_xnx)
