is_running = True
tasks = {1:"run", 2:"jog"}



def todo():
    global is_running, tasks
    while is_running:
        print("*********TO-DO-LIST**********")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Delete Tasks")
        print("5. Exit")
        print("******************************\n")

        choice = input("Choose an option: ")

        if choice == "1":
            if len(tasks) == 0:
                print("No Task avaliable yet😭😪 ")
            else:
                i = 0
                print("\n**********CURRENT TASKS**********")
                for key, values in tasks.items():
                    print(f"{key}: {values}")
                print("***********************************\n")
        elif choice == "2":
            c1 = (input("Enter Task: ")).lower()
            if c1 in tasks.values():
                print(f"{c1} is already in task list")
            else:
                tasks.update({len(tasks)+1:c1})
                print("task added successfully🎊🎊\n")
        elif choice == "3":
            print("=====taskes avaliable=====")
            for key, values in tasks.items():
                print(f"{key}: {values}")
            c2 = int(input("choose option of completed task: "))

            if c2 in tasks.keys():
                tasks[c2] = f'{tasks[c2]} (completed)✅' 
                print("Tasks list updated successfully🎊\n")
            else:
                print("option not in task\n")    
        elif choice == "4":
            print("=====taskes avaliable=====")
            for key, values in tasks.items():
                print(f"{key}: {values}")

            c3 = int(input("Enter option to delete: "))
            if c3 in tasks.keys():
                del tasks[c3]
                print("task deleted successfully✅✅\n")
            else:
                print("invalid option☠️☠️")
        elif choice == "5":
            is_running = False
        else:
            print("Invalid option😭☠️☠️")
            print("Try again👇👇\n")

    print("\nGoodbye✋👋👋")

todo()
if __name__  == "__main__ ":
    todo()
