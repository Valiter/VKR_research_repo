import pandas as pd
from scipy.stats import chi2_contingency
import sys

def calculate_phi_coefficient(file_path, col1, col2):
    # Читаем Excel
    df = pd.read_excel(file_path)

    # Проверяем, что столбцы есть
    if col1 not in df.columns or col2 not in df.columns:
        print(f"Ошибка: в файле нет столбцов {col1} или {col2}")
        return

    # Формируем таблицу сопряженности 2x2
    contingency_table = pd.crosstab(df[col1], df[col2])

    if contingency_table.shape != (2, 2):
        print("Ошибка: фи-коэффициент считается для таблицы 2x2. Проверьте, что обе переменные бинарные.")
        print("Текущая таблица сопряженности:")
        print(contingency_table)
        return

    # Вычисляем хи-квадрат и phi
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    n = contingency_table.to_numpy().sum()
    phi = (chi2 / n) ** 0.5

    print(f"Таблица сопряженности:\n{contingency_table}\n")
    print(f"Chi2 = {chi2:.4f}, p-value = {p:.4f}, n = {n}")
    print(f"Фи-коэффициент (φ) = {phi:.4f}")


col1 = 'Сказка'
col2 = 'Группа'
file_path = '/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Correlations/GroupAndBall.xlsx'
calculate_phi_coefficient(file_path, col1, col2)
