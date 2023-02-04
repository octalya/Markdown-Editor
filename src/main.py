import utils.formatters as formatters
import os

def main():
    prev_output = ""

    while True:

        print("Choose one of the formatters: plain, bold, italic, inline-code, header, link, ordered-list, unordered-list")
        formatter = input("Type a formatter of choice or type 'finish' (to exit a program and save the output):")

        match formatter:
            case "finish":
                break
            case "plain":
                prev_output = formatters.text_markdown(formatter, prev_output)
            case "bold":
                prev_output = formatters.text_markdown(formatter, prev_output)
            case "italic":
                prev_output = formatters.text_markdown(formatter, prev_output)
            case "inline-code":
                prev_output = formatters.text_markdown(formatter, prev_output)
            case "header":
                prev_output = formatters.header_markdown(formatter, prev_output)
            case "link":
                prev_output = formatters.link_markdown(formatter, prev_output)
            case "new-line":
                prev_output = formatters.new_line_markdown(formatter, prev_output)
            case "ordered-list":
                prev_output = formatters.list_markdown(formatter, prev_output)
            case "unordered-list":
                prev_output = formatters.list_markdown(formatter, prev_output)
            case _:
                print("Unknown formatting type or command")

        print(prev_output)

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
                print(f"Those are the available files in 'outputs' folder: {available_files}")
                name = input("Type the name of an file from a given choice:")
                mode = "a"
                break
            else:
                print("Unknown command. Please choose between 'new' and 'append'.")

    # saving output 
    file = open(f'src/outputs/{name}.md', mode, encoding='utf-8')
    file.writelines(prev_output)
    file.close()

if __name__ == "__main__":
    main()
