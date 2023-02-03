import formatters

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

    # saving output in "output.md" file
    file = open('output.md', 'w', encoding='utf-8')
    file.writelines(prev_output)
    file.close()

if __name__ == "__main__":
    main()
