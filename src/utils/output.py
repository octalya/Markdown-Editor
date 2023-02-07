import os

def new_file():
    while True:
        print("Requirements for the file name: filename should end with '.md' extension and have no additional periods and no spaces (ex: 'output.md')")
        name = input("Type the name of an output file:")
        if len(name.split(".")) != 2 or name.split(".")[1] != "md" or " " in name:
            print("Invalid input")
        else:
            break
    return name

def output_file(prev_output):

    if "outputs" not in os.listdir("src"):
        os.mkdir("src/outputs")

    while True:

        if len(os.listdir("src/outputs")) == 0:
            name = new_file()
            mode = "w"
            break
        else:
            print("Do you want to create a new file with a text or append to the existing one?")
            question = input("Type 'new' or 'append':")

            if question == "new":
                name = new_file()
                mode = "w"
                break

            elif question == "append":
                available_files = os.listdir("src/outputs")
                name = None
                while name not in available_files:
                    print(f"Those are the available files in 'outputs' folder: {available_files}")
                    name = input("Type the name of an file with extension from a given choice:")
                mode = "a"
                break
            else:
                print("Unknown command. Please choose between 'new' and 'append'.")

    # saving output 
    file = open(f'src/outputs/{name}', mode, encoding='utf-8')
    file.writelines(prev_output)
    file.close()
