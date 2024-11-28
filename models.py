import json



# Модель задачи
class Task():

    status: str = 'Не выполнена'

    def __init__(self, title: str, description: str, category: str, due_date: str, priority: str,  id: int=2):

        print(self._add_id())
        if id < 2:
            self.id = id
        else:
            self.id = self._add_id()
        self.title = title.capitalize()
        self.description = description.capitalize()
        self.category = category.capitalize()
        self.due_date = due_date.capitalize()
        self.priority = priority.capitalize()

    @classmethod
    def _add_id(cls):
        """Метод работает внутри класса и добавляет id задаче"""

        # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Присвоение задаче id
        if data['tasks']:
            id = data['tasks'][-1]['task_id'] + 1
        else:
            id = 2
        return id
        

    def del_task(id_or_category: int|str) -> bool:
        """Метод удаляет задачу из файла tasks.txt по id или категории"""

        # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        flag = False

        # Поиск задачи по id или категории и её удаление
        for task in data['tasks']:
            if task['task_id'] == id_or_category or task['task_category'] == id_or_category:
                data['tasks'].remove(task)
                with open('tasks.txt', 'w', encoding='utf-8') as file:
                    json.dump(data, file)
                print()
                print(f'Задача успешно удалена.')
                print()
                flag = True
        if flag:
            return True
        # Вывод ошибки, если задачи с таким id или категории нет в базе
        else:
            return False
    
    def add_task(self) -> str:
        """Метод добавляет задачу в файл tasks.txt"""

        # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        data['tasks'].append({
        'task_id': self.id,
        'task_title': self.title,
        'task_description': self.description,
        'task_category': self.category,
        'task_due_date': self.due_date,
        'task_priority': self.priority,
        'task_status': 'Не выполнена'
        })
        
        # Запись новой задачи в файл tasks.txt
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            json.dump(data, file)

        return f'Задача {self.title} успешно добавленна в базу с id {self.id}'
    
    def search_task(search: str) -> list:
        """Метод поиска задачи по ключевым словам, категории или статусу выполнения"""
        tasks = []

         # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if data['tasks']:
            for task in data['tasks']:
                # Непосредственно поиск задачи по ключевым словам, категории или статусу выполнения
                if search in task['task_title'].lower() or task['task_category'].lower() == search or task['task_status'] == search:
                    tasks.append(task)
        return tasks

    def edit_task(id: int, field: str, new_field: str) -> bool:
        """Метод находит задачу по id в файле tasks.txt и редактирует её"""

        # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        flag = False

        if data['tasks']:
            for task in data['tasks']:

                # Непосредственно редактирование задачи
                if task['task_id'] == id:
                    task[f'task_{field}'] = new_field.capitalize()
                    with open('tasks.txt', 'w', encoding='utf-8') as file:
                        json.dump(data, file)
            
                    flag = True
        if flag:
            print()
            print(f'Задача с id {id} успешно редактирована')
            print()
                    
            return True
        else:
            print()
            print(f'К сожалению задачи с id {id} у нас нет(')
            print()
            return False

    def view_tasks():
        """Метод выводит в консоль все задачи"""

        # Открытие файла tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Непосредственно вывод в консоль всех задач из базы
        if data['tasks']:
            print()
            print('Вот все задачи:')
            print()
            for task in data['tasks']:
                print(task['task_title'])
                print(task['task_description'])
                print(task['task_category'])
                print(task['task_due_date'])
                print(task['task_priority'])
                print(task['task_status'])
                print()
        # Вывод ошибки, если нет ни одной задачи в базе
        else:
            print('К сожалению в данный момент у нас нет ни одной задачи(')

    