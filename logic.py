from models import Task


# Добавление задачи
def add_task() -> bool:
    """Функция предлагает ввод из консоли названия, описания, категории, срок выполнения, приоритет и статус задачи,
      и записывает задачу в файл tasks.txt в формате json присваивая кзадаче id"""

    # Ввод названия и срока выполнения новой задачи
    title = input('Введите название задачи, которую хотите добавить: ').capitalize()
    # Проверка на то, что ввели не пустую строку
    if not title:
        print()
        print('Название задачи не может быть пустой! Надо начинать сначала!')
        print()
    due_date = input('Введите срок выполнения задачи, которую хотите добавить в формате ГГГГ-ММ-ДД: ')
    
    # Проверка на ввод срока выполнения
    if valid_date(due_date):
        print()
        print('То что Вы ввели не похоже на срок выполнения задачи в формате ГГГГ-ММ-ДД.! Надо начинать сначала!')
        print()
        return add_task()
    
    # Ввод приоритета новой задачи
    priority = input('Введите приоритет задачи, которую хотите добавить(Низкий, Средний, Высокий): ').capitalize()

    # Проверка на ввод приоритета
    if priority not in ['Низкий', 'Средний', 'Высокий']:
        print()
        print('То что Вы ввели не похоже на приоритет задачи! Надо начинать сначала!')
        print()
        return add_task()
    
    # Ввод описания и категории новой задачи
    description = input('Введите описание задачи, которую хотите добавить: ').capitalize()
    category = input('Введите категорию задачи, которую хотите добавить: ').capitalize()

    # Проверка на то, что ввели не пустую строку
    if not description and category:
        print()
        print('Описание и категория задачи не может быть пустой! Надо начинать сначала!')
        print()

    task = Task(title=title, description=description, category=category, due_date=due_date, priority=priority)

    print()
    print(task.add_task())
    print()
    
    return True

# Удаления задачи по id
def del_task() -> None:
    """Функция предлагает ввод из консоли id задачи, и удаляет задачу из файла tasks.txt"""

    # Ввод id
    task_id = input('Введите id задачи, которую Вы хотите удалить: ')

    # Проверка id, на то, что введённые данные являются числом
    if task_id.isdigit():

        if not Task.del_task(int(task_id)):
            print()
            print(f'Задачи с id {task_id} нет в нашем списке!')
            print()
            del_task()
    # Вывод ошибки, если введённое значение не является числом
    else:
        print()
        print('То, что Вы ввели не является числом!')
        print()
        del_task()

# Поиск задачи по ключевым словам, категории или статусу выполнения
def search_task() -> None:
    """Функция предлагает ввод из консоли ключевых слов, категории или статус выполнения задачи, и находит задачу в файле tasks.txt.
    Если поиск не увенчался успехом, то выводит соответствующее сообщение в консоль"""

    # Ввод ключевых словх, категории или статуса выполнения задачи
    search = input('Введите слово, категорию или статус выполнения задачи: ').lower()
    tasks = Task.search_task(search=search)
    if tasks:
        print()
        for task in tasks:
            print(task['task_title'])
            print(task['task_description'])
            print(task['task_category'])
            print(task['task_due_date'])
            print(task['task_priority'])
            print(task['task_status'])
            print()
    else:
        print()
        print('К сожалению такой задачи у нас нет(')
        print()

# Редактирование задачи
def edit_task() -> None:
    """Функция предлагает ввод из консоли id, поля задачи и новое значение поля, и найдя задачу в файле tasks.txt редактируя задачу"""

    # Ввод id
    task_id = input('Введите id задачи, которую нужно редактировать: ')

    fields = {1: 'title', 2: 'description', 3: 'category', 4: 'due_date', 5: 'priority', 6: 'status'}

    # Проверка id, на то, что введённые данные являются числом
    if not task_id.isdigit():
        print('То что Вы ввели не похоже на id!')
        edit_task()

    # Ввод поля задачи для редактирования
    print("Выберите поле которое хотите редактировать:")
    print()
    print(' 1 - Редактировать название.')
    print(' 2 - Редактировать описание.')
    print(' 3 - Редактировать категорию.')
    print(' 4 - Редактировать срок выполнения.')
    print(' 5 - Редактировать приоритет.')
    print(' 6 - Редактировать статус.')
    task_field = input('Введите номер поле которое хотите редактировать от 1 до 6: ')

    # Проверка на то, что введённое поле соответствует стандартам
    if task_field.isdigit() and (1 <= int(task_field) <= 6):
        task_field = int(task_field)
        new_field = input('Введите новое значение поля: ')
        if task_field < 4:

            # Проверка на то, что ввели не пустую строку
            if not new_field:
                print()
                print('Новое поле задачи не может быть пустым! Надо начинать сначала!')
                print()
            
            Task.edit_task(int(task_id), fields[task_field], new_field)
                
        if task_field == 4:
            # Проверка на ввод срока выполнения
            if valid_date(new_field):
                print()
                print('То что Вы ввели не похоже на срок выполнения задачи в формате ГГГГ-ММ-ДД.! Надо начинать сначала!')
                print()
                return edit_task()
            else:
                Task.edit_task(int(task_id), fields[task_field], new_field)

        if task_field == 5:
            if new_field.capitalize() in ['Низкий', 'Средний', 'Высокий']:
                Task.edit_task(int(task_id), fields[task_field], new_field)
            
            else:
                print()
                print('То что Вы ввели не похоже на приоритет! Надо начинать сначала!')
                print()
                return edit_task()
        if task_field == 6:
            if new_field.capitalize() in ['Выполнена', 'Не выполнена']:
                Task.edit_task(int(task_id), fields[task_field], new_field)
            
            else:
                print()
                print('То что Вы ввели не похоже на статус! Надо начинать сначала!')
                print()
                return edit_task()
        
    else:
        print('То что Вы ввели не похоже на число от 1 до 6!')
        edit_task()

# Функция валидации даты
def valid_date(date: str) -> bool:
    return (len(date.split('-')) != 3 or int(date.split('-')[0]) < 2024 or (1 > int(date.split('-')[1]) > 12) \
            or (1 > int(date.split('-')[2]) > 31))\
            or not (date.split('-')[0].isdigit() and date.split('-')[1].isdigit() and date.split('-')[2].isdigit())
