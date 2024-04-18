def get_todos(filepath="report.txt"):

    " " " This functions read the text file and give the list of content in the file " " "

    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath="report.txt"):
    with open(filepath, "w") as local_file:
        local_file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos("report.txt"))
    text = """My name is rink
    I am a humanoid.
    what are you"""
    print(text)

