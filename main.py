'''
# Stage 3/3
Task: Implement a separate function for each of the formatters.
Apart from exiting the program, it should save the final result of a session to a file, let's call it output.md. 
Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.
'''

prev_output = ""

# functions for different types of formatters
def text_markdown(formatter, prev_output):

    text = str(input("Text:"))
    if formatter == "plain":
        prev_output+=text
    elif formatter == "bold":
        prev_output = prev_output + "**" + text + "**"
    elif formatter == "italic":
        prev_output = prev_output + "*" + text + "*"
    elif formatter == "inline-code":
        prev_output = prev_output + "`" + text + "`"
    
    return prev_output


def header_markdown(formatter, prev_output):

    level = int(input("Level:"))

    if level in range(1,7):
        text = str(input("Text:"))
        prev_output = prev_output + level*"#" + " " + text + "\n"
    else:
        print("The level should be within the range of 1 to 6")
        header_markdown(formatter)
    
    return prev_output


def link_markdown(formatter, prev_output):

    label = str(input("Label:"))
    url = str(input("URL:"))
    prev_output = prev_output + "[" + label + "]" + "(" + url + ")"

    return prev_output


def new_line_markdown(formatter, prev_output):

    prev_output = prev_output + "\n"
    return prev_output


def list_markdown(formatter, prev_output):

    rows = int(input("Number of rows:"))

    if rows >0:

        if formatter == 'ordered-list':
            for i in range(1, rows+1):
                text = str(input(f'Row #{i}:'))
                prev_output = prev_output + f"{i}. {text}\n"

        else:
            for i in range(1, rows+1):
                text = str(input(f'Row #{i}:'))
                prev_output = prev_output + f"* {text}\n"

    else:
        print("The number of rows should be greater than zero")
        list_markdown(formatter)

    return prev_output


# calling functions from inputs
while True:

    formatter = str(input("Choose a formatter:"))

    if formatter in ["plain", "bold", "italic", "inline-code"]:
        prev_output = text_markdown(formatter, prev_output)
    elif formatter == "header":
        prev_output = header_markdown(formatter, prev_output)
    elif formatter == "link":
        prev_output = link_markdown(formatter, prev_output)
    elif formatter == "new-line":
        prev_output = new_line_markdown(formatter, prev_output)
    elif formatter == "ordered-list" or formatter == "unordered-list":
        prev_output = list_markdown(formatter, prev_output)
    elif formatter == "!done":
        break
    else:
        print("Unknown formatting type or command")

    print(prev_output)

# saving output in "output.md" file
file = open('output.md', 'w', encoding='utf-8')
file.writelines(prev_output)
file.close()

