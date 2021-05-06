# Elwin plays with Python

### Study Notes
[Intro to Python](https://github.com/getfutureproof/fp_guides_wiki/wiki/Intro-to-Python)

## Exercises

Make sure Python is installed:
- [Installing Python](https://github.com/getfutureproof/fp_guides_wiki/wiki/Installing-Python)

Alternatively you can run a Docker container:
- `docker run -it --name my_py --mount type=bind,source="$(pwd)",dst=/code python:3.9.1 bash`

_NB: name and bind mount optional but useful_ \
_NB: python version up to you - `python:latest` to be bang up to date_

Once you have access to Python, play around with the command line:
- [x] Open the Python interpreter. This should take you to the command prompt (>>>)
- [x] Can you do some maths?
- [x] Can you get python to print out some data?
- [x] Close the python command prompt, ideally with `exit()` but Ctrl-Z and then Enter on Windows, or Ctrl-D on Mac will get the job done if needed.


Lets write a Python file:
- [x] Open your editor of choice, create a new file and save it with the extension .py
- [x] Write a single print statement in the file. It should print out the saying ‘Hello world!’
- [x] Go back to the command prompt, navigate to the folder that your first python file is saved in. Type in python followed by the name of your file including the .py extension <br />
**Congrats! You can run python files on your machine**

Variables playground:
- [x] Create a variable that contains a whole number
- [x] Print out the type of that number using a built-in function
- [x] Change the type of the number to be a float
- [x] Write the following sentences and store it in a variable: I’m learning python for the very first time this morning! We’re having a great time.
- [x] Try doing this with a pair of double quotes ( “ ) and a pair of single quotes outside ( ‘ ). Can you notice a difference? <br />
_You might need to use the escape character `\` so that you can store the string surrounded by single quotes._
- [x] Use the escape character to print each sentence on a new line.
- [x] Print out the sentences all in upper case to show your excitement.
- [x] Split the paragraph into two sentences and store the first sentence in a new variable. You’ve just made your first list!
- [x] Create a list of three numbers. <br />
_Lists are denoted by `[]`, ordered and changeable_
- [x] Print out the first element of your list
- [x] Change the third element of your list
- [x] Create a tuple containing three strings. <br />
_Tuples are denoted by `()`, ordered and unchangeable_
- [x] Print out the last element of your tuple
- [x] Check if your tuple contains ‘hello’
- [x] Create a dictionary containing three pieces of information about you: your name, python skill level (on a scale of 1 - 5) and if you have had a coffee or not this morning.. <br />
_Dictionaries are made up of key, value pairs. Key’s will always be strings, values can be any data type. Dictionaries are denoted by `{}` and key, value pairs are separated by colons. Dictionaries are unordered, changeable and indexed_
- [x] Print out your name
- [x] Update your python skill level to be one level higher than you originally put it
- [x] Add another element that is a tuple that contains the other programming languages you know.
- [x] Create a set that contains your favourite foods
_Sets are denoted by `{}` and are unordered._
- [x] You cannot change existing items in a set, but you can add or remove items from it. Replace one of your favourite foods.
- [x] Print out how many items are in your set

Naming Variables:
- [x] Download the file named variable_names.py
- [x] Taking advice from PEP8, rename any variables which you think are not compliant.

Writing functions:
- [x] Create a new file.
- [x] Create two variables, one that contains the name of your hometown and one that contains statistics about your hometown.
- [x] Create a function that calculates the population density of your hometown, you might need to add more statistics to your statistics variables now.
- [x] Create a function that returns a sentence telling users the population density of your hometown
- [x] Call the function and print it out.
- [x] What happens if there is no hometown variable stored, can we put a default in place instead?
- [x] Can you reduce the number of lines of code you’ve written. Spend some time refactoring.