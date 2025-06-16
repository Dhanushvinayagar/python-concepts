import os

def create_file():
    with open(file_name, "w") as file:
        file.write("Hello World")
        file.close()

def read_file():
    with open(file_name, "r") as file:
        print(file.read())

def append_file():
    with open(file_name, "a") as file:
        file.write("\nNew line")
        file.close()

def delete_file():
    os.remove(file_name)

file_name = "file.txt"
create_file()
read_file()
append_file()
read_file()
delete_file()
