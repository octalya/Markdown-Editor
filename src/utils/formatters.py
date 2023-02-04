# functions for different types of formatters
def text_markdown(formatter, prev_output):

    text = str(input("Text:"))
    if formatter == "plain":
        prev_output+=text
    elif formatter == "bold":
        prev_output = f'{prev_output}**{text}**'
    elif formatter == "italic":
        prev_output = f'{prev_output}*{text}*'
    elif formatter == "inline-code":
        prev_output = f'{prev_output}`{text}`'
    
    return prev_output


def header_markdown(formatter, prev_output):

    level = int(input("Level:"))

    if level in range(1,7):
        text = str(input("Text:"))
        hash_level = level*"#"
        prev_output = f"{prev_output}{hash_level}{text}\n"
    else:
        print("The level should be within the range of 1 to 6")
        header_markdown(formatter)
    
    return prev_output


def link_markdown(formatter, prev_output):

    label = str(input("Label:"))
    url = str(input("URL:"))
    prev_output = f'{prev_output}[{label}]({url})'

    return prev_output


def new_line_markdown(formatter, prev_output):

    prev_output = f'{prev_output}\n'
    return prev_output


def list_markdown(formatter, prev_output):

    rows = int(input("Number of rows:"))

    if rows >0:

        if formatter == 'ordered-list':
            for i in range(1, rows+1):
                text = str(input(f'Row #{i}:'))
                prev_output = f"{prev_output}{i}. {text}\n"

        else:
            for i in range(1, rows+1):
                text = str(input(f'Row #{i}:'))
                prev_output = prev_output + f"{prev_output}* {text}\n"

    else:
        print("The number of rows should be greater than zero")
        list_markdown(formatter)

    return prev_output