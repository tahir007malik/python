class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def show_tasks(self):
        if not self.tasks:
            print(f'Your to-do list is empty!')
        else:
            print('Your tasks:')
            for idx, task in enumerate(self.tasks, 1):
                print(f'{idx}. {task}')
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: {task}')
    
    def remove_task(self, taskNumber):
        taskNumber = int(taskNumber)
        if 1 <= taskNumber <= len(self.tasks):
            removed_task = self.tasks.pop(taskNumber - 1)
            print(f'Task removed: {removed_task}')
        else:
            print('Invalid task number!')

# Database
userName = 'sam'
password = 'sam'

# Login screen
userNameCheck = input('enter username: ')
if userNameCheck == userName:
    passwordCheck = input('enter password: ')
    if passwordCheck == password:
        # Initiating instance
        obj = ToDoList()
        print(f'Welcome {userName} \U0001f600, to your To-Do list\n')
        print(f'What do you want to do?\n')
        while True:
            print()
            print(f'Press 1 for printing task in to-do list')
            print(f'Press 2 for adding task in to-do list')
            print(f'Press 3 for removing task in to-do list')
            print(f'Press C to exit program')
            userInput = input('Enter choice (1,2, 3 or C): ')
            if userInput == '1':
                obj.show_tasks()
            elif userInput == '2':
                addTaskInput = input('Enter task: ')
                obj.add_task(addTaskInput)
            elif userInput == '3':
                removeTaskInput = input('Enter task number: ')
                obj.remove_task(removeTaskInput)
            elif userInput.upper() == 'C':
                print('Exiting the program')
                break
            else:
                print('Invalid input')
    else:
        print(f'Try again! Incorrect password for {userName}')
else:
    print('No record with this username')