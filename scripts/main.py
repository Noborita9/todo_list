from task_manager import Task_Manager
from task_dao import Task_Dao
def main():
    db = "../todos.db"
    tm = Task_Manager(db)
    status = tm.create_task("Do Bed", "Just Do IT", 5.4, 1)
    if status.completed == True:
        print("Shit Working!")


if __name__ == "__main__":
    main()
