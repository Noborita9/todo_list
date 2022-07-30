from task_manager import Task_Manager
def main():
    db = "../todos.db"
    tm = Task_Manager(db)
    status = tm.create_task("Do Bed", "Just Do IT", 5.4, 1)
    new_status = tm.select_task()


if __name__ == "__main__":
    main()
