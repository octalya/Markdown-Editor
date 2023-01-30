'''
# Stage 3/3
Task: Implement a separate function for each of the formatters.
Apart from exiting the program, it should save the final result of a session to a file, let's call it output.md. 
Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.
'''
import formatters
prev_output = ""

availiable_formatters = ["plain", "bold", "italic", "inline-code", "header", "link", "ordered-list", "unordered-list"]

while True:

    default_question = str(input("Choose a formatter (type a formatter of choice) or finish (type 'finish')?:"))
    if default_question == "finish":
        break
    elif default_question in availiable_formatters:

        formatter = default_question

        match formatter:

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
    else:
        print("Unknown formatting type or command")

    print(prev_output)

# saving output in "output.md" file
file = open('output.md', 'w', encoding='utf-8')
file.writelines(prev_output)
file.close()

