import pandas as pd
from scipy.stats import mannwhitneyu

def mann_whitney_correlation(group0, group1):
    """
    Рассчитывает U-статистику Манна-Уитни и рангово-бисериальный коэффициент корреляции.

    Параметры:
    group0, group1 - pandas Series или массивы с данными двух групп.

    Возвращает:
    U - статистика Манна-Уитни
    p - p-value двустороннего теста
    r - рангово-бисериальный коэффициент корреляции
    """
    U, p = mannwhitneyu(group0, group1, alternative='two-sided')
    n1 = len(group0)
    n2 = len(group1)
    r = 1 - (2 * U) / (n1 * n2)
    return U, p, r

def analyze_excel(file_path, group_col=0):
    """
    Считывает Excel-файл, где первый столбец — бинарная группа (0/1),
    остальные — ранговые переменные.
    Рассчитывает для каждого рангового столбца U-тест и рангово-бисериальный коэффициент корреляции.

    Параметры:
    file_path - путь к Excel-файлу
    group_col - индекс или имя столбца с группой (по умолчанию 0)

    Возвращает:
    pandas DataFrame с результатами для каждой переменной
    """
    df = pd.read_excel(file_path)

    # Проверка бинарности группового столбца
    groups = df.iloc[:, group_col]
    unique_vals = set(groups.dropna().unique())
    if not unique_vals.issubset({0, 1}):
        raise ValueError("Групповой столбец должен содержать только 0 и 1")

    results = []

    # Перебираем все столбцы, кроме группового
    for col in df.columns.drop(df.columns[group_col]):
        data = df[col]

        # Проверяем, что данные числовые
        if not pd.api.types.is_numeric_dtype(data):
            print(f"Пропускаем столбец '{col}', так как он не числовой")
            continue

        # Разделяем данные по группам
        group0 = data[groups == 0].dropna()
        group1 = data[groups == 1].dropna()

        # Проверяем, что обе группы не пусты
        if len(group0) == 0 or len(group1) == 0:
            print(f"Пропускаем столбец '{col}', так как одна из групп пуста")
            continue

        # Рассчитываем статистику и коэффициент
        try:
            U, p, r = mann_whitney_correlation(group0, group1)
            results.append({
                'Variable': col,
                'U_statistic': U,
                'p_value': p,
                'Rank_Biserial_Correlation': r
            })
        except Exception as e:
            print(f"Ошибка при обработке столбца '{col}': {e}")

    return pd.DataFrame(results)

# Пример использования
if __name__ == "__main__":
    file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/Mann Yitny/MANNYITNY.xlsx'  # Замените на путь к вашему файлу
    results_df = analyze_excel(file_path)
    print(results_df)
