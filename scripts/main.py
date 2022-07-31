from menu import Menu


def main():
    session = Menu("../todos.db")
    session.start()


if __name__ == "__main__":
    main()
