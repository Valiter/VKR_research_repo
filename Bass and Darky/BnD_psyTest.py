# Вставьте ваш текст сюда
input_string = """Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Да
Нет	Да	Да	Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет
Нет	Да	Нет	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет
Нет	Да	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да
Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да
Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет
Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет
Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Да	Да	Да
Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Да	Да	Да
Нет	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет
Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет
Нет	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет
Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да
Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да
Нет	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет
Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет
Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Нет
Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да
Нет	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет
Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да
Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет
Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет
Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет
Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет
Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да
Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет
Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет
Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Нет
Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет
Нет	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет
Нет	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да
Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да
Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет
Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет
Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да
Нет	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Нет
Нет	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да
Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Да	Да	Нет
Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет
Нет	Да	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Да	Нет
Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Нет
Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да
Нет	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да
Нет	Да	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Да
Нет	Да	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет
Нет	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Да
Нет	Да	Да	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да
Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Да	Нет
Нет	Да	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Да	Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Да	Да	Да	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Да
Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет
Нет	Да	Да	Нет	Нет	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Да	Да	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Да	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да
Нет	Нет	Да	Да	Да	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Да	Нет	Нет	Да	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Да	Да	Да	Нет	Нет	Да	Нет	Да	Да	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Да	Нет	Да	Да	Да	Да
Нет	Да	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Да	Да	Да	Нет
Нет	Да	Да	Да	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Да	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет	Нет	Да	Нет	Нет	Нет	Да	Да	Нет	Да	Нет	Да	Нет	Нет	Да	Нет	Нет	Нет	Нет	Нет	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Да	Да	Нет	Да	Да	Нет	Нет	Нет	Нет	Да	Нет	Да	Нет	Нет	Нет"""

# Функция для преобразования "Да"/"Нет" в 1/0
def yes_no_to_binary(word):
    word = word.strip().lower()
    if word == "да":
        return 1
    elif word == "нет":
        return 0
    else:
        raise ValueError(f"Неизвестное значение: {word}")

# Обработка строк
rows = [row for row in input_string.strip().split('\n') if row.strip()]
binary_rows = []
total_yes = 0
total_no = 0

for row in rows:
    words = row.split('\t')
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
