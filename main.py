'''
Stage 1/3 
Task: Print the source (raw) markdown code of the markdown snippet (can be found in images/task_1.png). 
Show your understanding of the syntax basics. 
'''

print('''
# John Lennon
or ***John Winston Ono Lennon*** was one of *The Beatles.*

Here are the songs he wrote I like the most:
- Imagine
- Norwegian Wood
- Come Together
- In My Life
- ~~Hey Jude~~ (that was *McCartney*)
''')

'''
# Stage 2/3
Task: Ask a user for input: `Choose a formatter`:.

- If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.
- If the input contains no formatters or unknown command is sent, print the following message and ask for input again: `Unknown formatting type or command.`
- If the input contains `!help`, print the list of available commands. 
- If the input contains `!done`, exit the editor without saving.
'''

availiable_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]

while True:
    formatter = str(input("Choose formatter:"))
    if formatter in availiable_formatters:
        continue
    elif formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif formatter == "!done":
        break
    else:
        print("Unknown formatting type or command")

'''
# Stage 3/3
Task: Implement a separate function for each of the formatters.
Apart from exiting the program, it should save the final result of a session to a file, let's call it output.md. 
Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.
'''

prev_output = ""

# functions for different types of formatters
def text_markdown(formatter):

    global prev_output

    text = str(input("Text:"))
    if formatter == "plain":
        prev_output+=text
    elif formatter == "bold":
        prev_output = prev_output + "**" + text + "**"
    elif formatter == "italic":
        prev_output = prev_output + "*" + text + "*"
    elif formatter == "inline-code":
        prev_output = prev_output + "`" + text + "`"


def header_markdown(formatter):

    global prev_output

    level = int(input("Level:"))

    if level in range(1,7):
        text = str(input("Text:"))
        prev_output = prev_output + level*"#" + " " + text + "\n"
    else:
        print("The level should be within the range of 1 to 6")
        header_markdown(formatter)

def link_markdown(formatter):

    global prev_output
    label = str(input("Label:"))
    url = str(input("URL:"))
    prev_output = prev_output + "[" + label + "]" + "(" + url + ")"

def new_line_markdown(formatter):

    global prev_output 

    prev_output = prev_output + "\n"

def list_markdown(formatter):

    global prev_output

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

# calling functions from inputs
while True:

    formatter = str(input("Choose a formatter:"))

    if formatter in ["plain", "bold", "italic", "inline-code"]:
        text_markdown(formatter)
    elif formatter == "header":
        header_markdown(formatter)
    elif formatter == "link":
        link_markdown(formatter)
    elif formatter == "new-line":
        new_line_markdown(formatter)
    elif formatter == "ordered-list" or formatter == "unordered-list":
        list_markdown(formatter)
    elif formatter == "!done":
        break
    else:
        print("Unknown formatting type or command")

    print(prev_output)

# saving output in "output.md" file
file = open('output.md', 'w', encoding='utf-8')
file.writelines(prev_output)
file.close()

