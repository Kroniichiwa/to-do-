# Define an empty dictionary to store the to-do list
lists = {}

def update():
    if lists :
        task_name = input("Enter the task name to update: ")
        if task_name in lists:
            if lists[task_name] == True :
                lists[task_name] = False
                print(f"Task '{task_name}' updated to Not Completed.")
            elif lists[task_name] == False :
                lists[task_name] = True
                print(f"Task '{task_name}' marked as Completed.")
        else:
            print(f"Task '{task_name}' not found in the to-do list.")
    else:
        print("The to-do list is empty.")


def add():
    task = input("Type your task : ")
    lists[task] = False
    print(f"Added {task} in the list!")

def delete() :
    task_name = input("Enter the task name to delete: ")
    if task_name in lists:
        del lists[task_name]
        print(f"Task '{task_name}' deleted.")
    else:
        print(f"Task '{task_name}' not found in the to-do list.")


def main():
    while True :

        print("Welcome to '"' TO DO LIST '"' program! ")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Quit the program")

        try :
            user_choice = int(input("Choose the number : "))
            if user_choice > 5 or user_choice < 1 :
                print("Please choose only 1-5 ")
                print("______________________")
            else :
                if user_choice == 1 :
                    add()
                    print("______________________")
                elif user_choice == 2 :
                    if lists :
                        for task, completed in lists.items():
                            print(f"{task}: {'Completed' if completed else 'Not Completed'}")
                            print("______________________")
                    else:
                        print("The to-do list is empty.")
                        print("______________________")
                elif user_choice == 3 :
                    update()
                    print("______________________")
                elif user_choice == 4 :
                    delete()
                    print("______________________")
                elif user_choice == 5 :
                    print("Good bye!")
                    break

        except :
            print("Please input only number!")



if __name__ == '__main__':
    main()