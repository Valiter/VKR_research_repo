import pandas as pd
import numpy as np

def filter_correlations_by_stars(input_file, output_file, significance_offset=1):
    """
    Загружает Excel-файл с корреляционной матрицей и значимостью,
    очищает все корреляции и значимости, если в ячейке корреляции нет звездочек,
    и сохраняет результат в новый файл.

    Параметры:
    - input_file: путь к исходному Excel-файлу
    - output_file: путь для сохранения отфильтрованного файла
    - significance_offset: сколько строк вниз от корреляции находится значимость (обычно 1)
    """

    df = pd.read_excel(input_file, header=None)

    # Названия столбцов (первая строка, начиная со второго столбца)
    col_names = df.iloc[0, 1:].astype(str).str.strip().tolist()

    # Названия строк (второй столбец, начиная со второй строки)
    row_names = df.iloc[1:, 1].astype(str).str.strip().tolist()

    result_df = df.copy()

    # Проходим по всем строкам и столбцам корреляционной матрицы
    # i - индекс строки в df (начинается с 1, т.к. 0 - заголовок)
    # j - индекс столбца в df (начинается с 1, т.к. 0 - первый столбец с названиями)
    for i in range(1, 1 + len(row_names)):
        for j in range(1, 1 + len(col_names)):
            corr_cell = df.iat[i, j]

            # Проверяем наличие звездочек в ячейке корреляции
            if not (isinstance(corr_cell, str) and ('*' in corr_cell)):
                # Очищаем корреляцию и значимость
                result_df.iat[i, j] = np.nan
                sig_row = i + significance_offset
                if sig_row < len(df):
                    result_df.iat[sig_row, j] = np.nan

    result_df.to_excel(output_file, index=False, header=False)
    print(f"Отфильтрованный файл сохранён: {output_file}")

if __name__ == "__main__":
    input_path = "/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/files_exel/КорреляцииВСЕХ_UPD_v3.xlsx"
    output_path = "/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/colored_files_exel/отфильтрованный_файл_ALL.xlsx"
    filter_correlations_by_stars(input_path, output_path)
