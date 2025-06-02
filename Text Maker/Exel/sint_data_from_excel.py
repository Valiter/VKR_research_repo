import pandas as pd
import re


def analyze_correlation_tables(input_files):
    """
    Анализирует три Excel-файла с корреляционными матрицами,
    где названия строк берутся из второго столбца,
    а названия столбцов — из первой строки, начиная со второго столбца.

    Возвращает DataFrame с найденными значимыми корреляциями (со звездочками).
    """
    column_names = ["ВСЕ", "ВРАЧИ", "ПСИХОЛОГИ"]
    dataframes = []
    for file_path in input_files:
        df = pd.read_excel(file_path, header=None)
        dataframes.append(df)

    main_df = dataframes[0]

    # Названия столбцов — из первой строки, начиная со второго столбца (индекс 1)
    column_names_list = main_df.iloc[0, 1:].dropna().astype(str).tolist()

    # Названия строк — из второго столбца, начиная со второй строки (индекс 1)
    row_names_list = main_df.iloc[1:, 1].dropna().astype(str).tolist()

    start_row = 1  # индекс первой строки с данными
    start_col = 1  # индекс первого столбца с данными

    results = []

    for row_offset, row_name in enumerate(row_names_list):
        row_idx = start_row + row_offset
        for col_offset, col_name in enumerate(column_names_list):
            col_idx = start_col + col_offset

            # Пропускаем диагональные элементы (корреляция переменной с собой)
            if row_name == col_name:
                continue

            cell_value = main_df.iat[row_idx, col_idx]

            if pd.notna(cell_value) and isinstance(cell_value, str) and ('*' in cell_value):
                # Извлекаем числовое значение корреляции без звездочек
                correlation_str = re.sub(r'\*+', '', cell_value)
                try:
                    correlation_value = float(correlation_str)
                except:
                    continue

                # Значимость - ячейка под текущей (row_idx + 1, col_idx)
                significance_value = None
                sig_row_idx = row_idx + 1
                if sig_row_idx < len(main_df):
                    sig_cell = main_df.iat[sig_row_idx, col_idx]
                    if pd.notna(sig_cell):
                        try:
                            significance_value = float(sig_cell)
                        except:
                            significance_value = str(sig_cell)

                variable_pair = f"{row_name} × {col_name}"

                # Ищем корреляции в других файлах
                correlations_other_files = []
                for df in dataframes[1:]:
                    other_corr = None
                    other_sig = None
                    try:
                        # Найдем индекс строки с row_name во втором столбце (индекс 1)
                        other_row_idx = df.index[df.iloc[:, 1] == row_name].tolist()
                        # Найдем индекс столбца с col_name в первой строке (индекс 0)
                        other_col_idx = df.columns[df.iloc[0, :] == col_name].tolist()

                        if other_row_idx and other_col_idx:
                            r_idx = other_row_idx[0]
                            c_idx = other_col_idx[0]
                            other_cell = df.iat[r_idx, c_idx]
                            if pd.notna(other_cell):
                                if isinstance(other_cell, str):
                                    other_corr_str = re.sub(r'\*+', '', other_cell)
                                else:
                                    other_corr_str = other_cell
                                try:
                                    other_corr = float(other_corr_str)
                                except:
                                    other_corr = other_cell

                                # Значимость под этой ячейкой
                                sig_r_idx = r_idx + 1
                                if sig_r_idx < len(df):
                                    other_sig_cell = df.iat[sig_r_idx, c_idx]
                                    if pd.notna(other_sig_cell):
                                        try:
                                            other_sig = float(other_sig_cell)
                                        except:
                                            other_sig = other_sig_cell
                    except Exception:
                        other_corr = None
                        other_sig = None

                    correlations_other_files.append((other_corr, other_sig))

                result_row = {
                    'Переменные': variable_pair,
                    'ВСЕ_корреляция': correlation_value,
                    'ВСЕ_значимость': significance_value,
                    'ВРАЧИ_корреляция': correlations_other_files[0][0] if len(correlations_other_files) > 0 else None,
                    'ВРАЧИ_значимость': correlations_other_files[0][1] if len(correlations_other_files) > 0 else None,
                    'ПСИХОЛОГИ_корреляция': correlations_other_files[1][0] if len(
                        correlations_other_files) > 1 else None,
                    'ПСИХОЛОГИ_значимость': correlations_other_files[1][1] if len(
                        correlations_other_files) > 1 else None,
                    'Звездочки': cell_value
                }

                results.append(result_row)

    if results:
        result_df = pd.DataFrame(results)
        result_df['abs_correlation'] = result_df['ВСЕ_корреляция'].apply(
            lambda x: abs(x) if isinstance(x, (int, float)) else 0)
        result_df = result_df.sort_values('abs_correlation', ascending=False).drop('abs_correlation', axis=1)
        return result_df
    else:
        print("Не найдено значимых корреляций со звездочками")
        return pd.DataFrame()


def save_results(result_df, output_path):
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            result_df.to_excel(writer, sheet_name='Значимые_корреляции', index=False)
        print(f"Результаты сохранены в файл: {output_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    input_data = [
        '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/files_exel/КорреляцииВСЕХ_UPD_v3.xlsx',
        '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/files_exel/КорреляцииВрачи_UPD_v3.xlsx',
        '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/files_exel/КорреляцииПсихологи_UPD_v3.xlsx'
    ]

    result = analyze_correlation_tables(input_data)

    if result is not None and not result.empty:
        print(f"\nНайдено {len(result)} значимых корреляций")
        print("\nПервые 10 строк результата:")
        print(result.head(10))

        output_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Text Maker/Exel/files_exel/Анализ_значимых_корреляций.xlsx'
        save_results(result, output_path)

        # Подсчёт статистики по звёздочкам
        count_double_stars = result['Звездочки'].str.contains(r'\*\*', na=False).sum()
        count_single_star = result['Звездочки'].apply(
            lambda x: ('*' in x) and ('**' not in x) if isinstance(x, str) else False
        ).sum()

        print(f"\nСтатистика:")
        print(f"Всего значимых корреляций: {len(result)}")
        print(f"Корреляции с **: {count_double_stars}")
        print(f"Корреляции с *: {count_single_star}")
    else:
        print("Анализ не дал результатов")
