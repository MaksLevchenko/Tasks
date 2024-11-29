import json
import os

from logic import add_task, del_task, search_task, edit_task
from models import TaskManager


# Главная функция программы
def main():

    # Вывод в консоль подсказки с доступными командами
    print('Что Вы хотите сделать? Введите один из вариантов от 1 до 5: ')
    print(' 1 - Добавить задачу.')
    print(' 2 - Удалить задачу.')
    print(' 3 - Поиск задачи.')
    print(' 4 - Все задачи.')
    print(' 5 - Редактировать задачу.')

    # Ввод команды
    action = input()

    # Проверка на то, что команда является числом от 1 до 5
    if not action.isdigit() or int(action) <= 0 or int(action) > 5:
        print('Я Вас не понял:')
        main()
    else:
        # Если команда является числом от 1 до 5 запускаем соответствующую функцию
        if int(action) == 1:
            add_task()
        elif int(action) == 2:
            del_task()
        elif int(action) == 3:
            search_task()
        elif int(action) == 4:
            TaskManager.view_tasks()
        elif int(action) == 5:
            edit_task()

# Создаём файл tasks.txt, если его ещё нет
if os.path.exists('tasks.txt'):
    data = {}
    data['tasks'] = []
    with open('tasks.txt', 'r', encoding='utf-8') as file:
        data_1 = file.readline()
    if not data_1:
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            json.dump(data, file)
else:
    data = {}
    data['tasks'] = []
    with open('tasks.txt', 'a', encoding='utf-8') as file:
        json.dump(data, file)

if __name__ == "__main__":

    # Запускаем бесконечный цикл
    while True:
        # Вызываем функцию main
        main()