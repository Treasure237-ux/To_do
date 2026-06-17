is_running = True
tasks = ["run","jog"]

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
                for task in tasks:
                    i += 1
                    print(f"{i}. {task}")
                print("***********************************\n")
        elif choice == "2":
            c1 = input("Enter Task: ")
            if c1 in tasks:
                print(f"{c1} is already in task list")
            else:
                tasks.append(c1)
                print("task added successfully🎊🎊\n")
        elif choice == "3":
            i = 0
            print("=====taskes avaliable=====")
            for task in tasks:
                i += 1
                print(f"{i}. {task}")
            c2 = input("choose option of completed task: ")
            for j in task:
                return j

            if c2 == j:
                tasks[int(j)-1] = f'{tasks[int(j)-1]} (completed)✅' 
                print("Tasks list updated successfully🎊\n")
            else:
                print("option not in task\n")
             
        elif choice == "4":
            pass
        elif choice == "5":
            is_running = False
        else:
            print("Invalid option😭☠️☠️")
            print("Try again👇👇\n")

    print("\nGoodbye✋👋👋")

todo()
if __name__  == "__main__ ":
    todo()
