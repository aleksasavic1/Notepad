import os

def create_a_new_notepad_file():
    notepad = input("Enter a Notepad name: ")
    file_name = f"notepad/{notepad}.txt"

    with open(file_name, "w") as f:
        pass

    print(f"Notepad has been added to the folder: {file_name}")


def enter_text_in_notepad():
    open_notepad = input("Enter the name of the Notepad you want to \
open (without .txt): ")
    path = f"notepad/{open_notepad}.txt"

    print("Press Enter for a new line each time.\n(When you're done, enter ~)")

    while True:
        text = input("Enter the text you want in your Notepad: ")
        if text == "~":
            break

        with open(path, "a") as f:
            f.write(text + "\n")


def remove_notepad():
    try:
        file_name = input("Enter the name of the Notepad you want to \
remove (without .txt): ")
        path = f"notepad/{file_name}.txt"
        os.remove(path)
        print(f"The file {file_name}.txt has been removed.")

    except FileNotFoundError:
        print(f"The file {file_name}.txt does not exist.")


def read_your_notepad():
    try:
        file_name = input("Enter the name of the Notepad you want to \
read (without .txt): ")
        path = f"notepad/{file_name}.txt"

        with open(path, "r") as f:
            content = f.read()
            print(f"\n{content}")

    except FileNotFoundError:
        print(f"The file {file_name}.txt does not exist.")


while True:
    print("\n1. Create a new Notepad file\n2. Enter text in Notepad\
\n3. Remove Notepad\n4. Read your Notepad\n5. Exit")

    choice = input("Choose an option (1/2/3/4/5): ")

    if choice == "1":
        create_a_new_notepad_file()

    elif choice == "2":
        enter_text_in_notepad()
    
    elif choice == "3":
        remove_notepad()

    elif choice == "4":
        read_your_notepad()

    elif choice == "5":
        print("Thank you for using the program!")
        break

    else:
        print("Error! Please choose an option (1/2/3/4/5)")
