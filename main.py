from argparse import ArgumentError


class ToDo:

    def __init__(self, name) -> None:
        '''constructor'''
        if str(name) == "" or name is None:
            raise ArgumentError("name cannot be null")
        self.name = name
        self.completed = False

    def mark_complete(self):
        self.completed = True

class ToDoList:

    def __init__(self) -> None:
        self.todos = []

    def add(self, todo:ToDo):
        self.todos.append(todo)

'''main program codes'''
todo_list = ToDoList()
todo_list.add(ToDo("Make a GitHub repo"))
todo_list.add(ToDo("Write some Pythons"))

for todo in todo_list.todos:
    print(todo.name)
