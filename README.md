# Markdown Editor
Markdown is a markup language with plain text formatting syntax. In this repository you can find an editor that allows the creation of markdown-compliant strings and save results to an "output" file.

 *This project is created by following the instructions from **JetBrains Academy course**.*

## Requirements

- Python 3.10 or above


## Installation

In order to test the script please run the following commands:

```python
# clone the repository
git clone https://github.com/octalya/Markdown-Editor
# run main.py
python src/main.py
```

## Usage

To find out about the markdown syntax follow [this guide](https://www.markdownguide.org/basic-syntax/)

**Answer the default question:** *Type a formatter of choice or type 'finish' (to exit a program and save the output):*

- to write a text in a particular markdown style: type a formatter of choice from the given list:

    - ***bold***
    - ***italic***
    - ***inline-code***
    - ***header***
    - ***link***
    - ***ordered-list***
    - ***unordered-list***

    then follow the instructions in following questions by typing the text you would like to be formatted and satisfying any other requirements for a particular formatter

- to finish writing a text: type ***finish***

**Save markdown-formatted string in the file**
 - if this is your first generated text using this program, you will need to answer question: *Type the name of an output file in a text format without spaces:* and type the name of the file that will be saved in `.md` format in *outputs* directory

 - otherwise, answer the other question: *Do you want to create a new file with a text or append to the existing one?* and type either ***append*** or ***new*** and follow further instructions for saving the outputs of the program






