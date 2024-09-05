def write_file(file_name, file_content):
    with open(str(file_name) + "txt",mode = "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(str(file_name) + "txt", mode="a") as file:
        file.write(append_content)

def read_file(file_name):
    with open(str(file_name) + "txt", mode="r") as file:
        print(file.read())
