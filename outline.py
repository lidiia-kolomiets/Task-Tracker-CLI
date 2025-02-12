import os, random, json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file or returns an empty list if the file doesn't exist or is corrupted."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            return eval(content) if content else []  # Using eval to parse JSON manually
    except (SyntaxError, NameError):
        print("Warning: JSON file is corrupted. Resetting tasks.")
        return []

def save_tasks(tasks):
    """Saves the tasks to a JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            task_serializable = json.dumps(task.to_dict())#теперь предыдущий ввод не сохраняется
            file.write(task_serializable)
def add(task):#не поддерживает добавление нескольких задач одновременно 
    tasks = load_tasks()
    task = Task()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

class Task():
    def __init__(self, name, status=None, id=None):#зачем id=None#как сделать так, чтобы аргумент add или другой команды записывался в качестве name
        self.id = self.calc_id()
        self.status = status
        self.name = name
    def calc_id(self):
        self.id = random.randint(10**3, 10**5)
    def to_dict(self):#добавить применение метода
        return {"id": self.id, "status": self.status}
    
#я комбинирую ооп и процедурное программирование. так можно?        
def list_tasks():#какие требования к реализации
    tasks = load_tasks()
    if tasks:
        print("\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks)))
    else:
        print("No tasks found.")

def update_task():#task or several tasks at a time
    pass



def main():
    commands = {
        "add": add,
        "list": list_tasks
    }
    while True:
        inp = input("Enter command: ").strip().lower().split(maxsplit=1)
        command = inp[0]
        args = inp[1:] if len(inp) > 1 else ""

        if command in commands:
            commands[command](args)
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
#не забудь commit, как только будет готова первая ф-ия с покрытием тестами
    
    