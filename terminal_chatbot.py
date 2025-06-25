class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number!")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    task_manager = TaskManager()
    
    print("Welcome to Task Manager Chatbot!")
    print("Type 'menu' at any time to see options or 'exit' to quit.")
    
    while True:
        user_input = input("\nWhat would you like to do? ").strip().lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'menu':
            print("\nMenu Options:")
            print("1. add <task> - Add a new task")
            print("2. remove <number> - Remove a task by its number")
            print("3. list - List all tasks")
            print("4. exit - Exit the program")
        elif user_input.startswith('add '):
            task = user_input[4:].strip()
            if task:
                task_manager.add_task(task)
            else:
                print("Please specify a task to add.")
        elif user_input.startswith('remove '):
            try:
                task_num = int(user_input[7:].strip())
                task_manager.remove_task(task_num - 1)
            except ValueError:
                print("Please enter a valid task number.")
        elif user_input == 'list':
            task_manager.list_tasks()
        elif user_input in ['1', '2', '3', '4']:
            # Alternative menu-based interface
            if user_input == '1':
                task = input("Enter task to add: ").strip()
                if task:
                    task_manager.add_task(task)
                else:
                    print("Task cannot be empty!")
            elif user_input == '2':
                task_manager.list_tasks()
                if task_manager.tasks:
                    try:
                        task_num = int(input("Enter task number to remove: ").strip())
                        task_manager.remove_task(task_num - 1)
                    except ValueError:
                        print("Please enter a valid number.")
            elif user_input == '3':
                task_manager.list_tasks()
            elif user_input == '4':
                print("Goodbye!")
                break
        else:
            print("Invalid command. Type 'menu' to see options.")

if __name__ == "__main__":
    main()