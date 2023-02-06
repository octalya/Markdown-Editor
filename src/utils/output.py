import os

def output_file(prev_output):

    while True:

        if len(os.listdir("src/outputs")) == 0:
            name = input("Type the name of an output file in a text format without spaces:")
            mode = "w"
            break
        else:
            print("Do you want to create a new file with a text or append to the existing one?")
            question = input("Type 'new' or 'append':")
            if question == "new":
                name = input("Type the name of an output file in a text format without spaces:")
                mode = "w"
                break
            elif question == "append":
                available_files = os.listdir("src/outputs")
                name = None
                while name not in available_files:
                    print(f"Those are the available files in 'outputs' folder: {available_files}")
                    name = input("Type the name of an file from a given choice:")
                mode = "a"
                break
            else:
                print("Unknown command. Please choose between 'new' and 'append'.")

    # saving output 

    # edge case where the user can type the name of the file with the extension
    name = name.split(".md")[0]
    file = open(f'src/outputs/{name}.md', mode, encoding='utf-8')
    file.writelines(prev_output)
    file.close()
