class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Completed)"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks found.")


def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task as completed")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
