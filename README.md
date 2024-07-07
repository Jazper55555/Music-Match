<!-- ## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) -->

# Music Match - A Music Assignment CLI 

Welcome to *Music Match*, an interactive CLI that allows you to keep track of your students, music, and most importantly, their part assignments. As a music educator who teaches 6th-12th graders across four different campuses, it can become pretty daunting when it comes to organizing all of their info (including music assignments). This is an app to help alleviate some of the hassle associated with that task.

## Walkthrough

Watch this interactive walk through to see the app in action or read below in order to get a detailed description of the CLI and its functions.

## Installation

Fork and clone a copy of this repository.

You will need python3 and pip installed in order to run the program on your CLI. Once forked and cloned, run the following commands:

```python
pipenv install
pipenv shell
```

## Running the CLI

Once the python packages are installed, you will need to cd (change directory) to the lib folder and run the *debug.py* file. This will fill the databases with some basic seed data that you can interact with. Once the database has seed data, you can run the app itself *cli.py*:

```python
cd lib 
python debug.py 
^d
python cli.py
```

## File Overview

Below, you will find the *Directory Tree Structure*, *File Introductions*, and *Database Structure* which all have basic breakdowns of the included files.

## Directory Tree Structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── part.py
    │   └── piece.py
    │   └── student.py
    ├── cli.py
    ├── debug.py
    ├── pieces_cli.py
    ├── select_students_cli.py
    ├── students_cli.py
└── music_assignments.db

```

## File Introductions

Each py file in the *Directory Tree Structure* has a brief breakdown found below:

__lib/__
* cli.py = Contains *Greeting* and *Menu* methods for the main CLI
* debug.py = Contains seed data for the database and interactivity within the CLI
* pieces_cli.py = Contains CRUD methods for the *Pieces* menu in the CLI
* students_cli.py = Contains CRUD methods for the *Students* menu in the CLI
* select_student_cli.py = Contains CRUD methods for *Parts* found in the *Student* menu

__lib/models__
* `__init__.py` = Assigns the database to the appropriate python files
* part.py = Contains init, property, and class methods for the __Parts__ table in the database
* piece.py = Contains init, property, and class methods for the __Pieces__ table in the database
* student.py = Contains init, property, and class methods for the __Student__ table in the database

