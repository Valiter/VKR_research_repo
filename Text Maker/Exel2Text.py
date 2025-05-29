import pandas as pd


def create_files_from_excel(file_path):
    # Чтение Excel файла без заголовков
    df = pd.read_excel(file_path, header=None)

    # Для каждой строки первого столбца создаем отдельный файл
    for i in range(len(df)):
        with open(f'file_{i + 1}.txt', 'w', encoding='utf-8') as f:
            f.write(str(df.iloc[i, 0]))


create_files_from_excel('/Users/antonkuzmichev/VKR_researching/VKR_research_repo/Story Read/Stories.xlsx')
