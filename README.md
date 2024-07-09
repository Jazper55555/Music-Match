# Music Match - A Music Assignment CLI 

Welcome to *Music Match*, an interactive CLI that allows you to keep track of your students, music, and most importantly, their part assignments. As a music educator who teaches 6th-12th graders across four different campuses, it can become pretty daunting when it comes to organizing all of their info (including music assignments). This is an app to help alleviate some of the hassle associated with that task.

### Walkthrough

Watch this interactive walk through to see the app in action or read below in order to get a detailed description of the CLI and its functions.

### Installation

Fork and clone a copy of this repository.

You will need python3 and pip installed in order to run the program on your CLI. Once forked and cloned, run the following commands:

```python
pipenv install
pipenv shell
```

### Running the CLI

Once the python packages are installed, you will need to cd (change directory) to the lib folder and run the *debug.py* file. This will fill the databases with some basic seed data that you can interact with. Once the database has seed data, you can run the app itself *cli.py*:

```python
cd lib 
python debug.py 
^d
python cli.py
```

## File Struture

Below, you will find the *Directory Tree Structure*, *Database Structure*, and *File Overview* sections which all have basic breakdowns of the included files.

### Directory Tree Structure

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

### Database Structure

__music_assignments.db__

The database is composed of 3 tables corresponding to the *student.py*, *piece.py*, and *part.py* files. Each file contains full CRUD methods for creating, reading, updating, and deleting data within the corresponding tables (as well as the CLI).

### File Overview

Each .py file in the *Directory Tree Structure* has a brief breakdown found below:

__lib/__
* `cli.py` = Contains *Greeting* and *Menu* methods for the main CLI
* `debug.py` = Contains table creation & seed data for the database and interactivity within the CLI
* `pieces_cli.py` = Contains CRUD methods for the __Pieces__ menu in the CLI
* `students_cli.py` = Contains CRUD methods for the __Students__ menu in the CLI
* `select_student_cli.py` = Contains CRUD methods for __Parts__ found in the *Student* sub-menu

__lib/models__
* `__init__.py` = Assigns the database to the appropriate python files
* `part.py` = Contains init, property, and class methods for the __Parts__ table in the database
* `piece.py` = Contains init, property, and class methods for the __Pieces__ table in the database
* `student.py` = Contains init, property, and class methods for the __Student__ table in the database

## Table Relationships

There are 3 data tables that form various relationships between them:

Student to Part: One to Many Relationship
Piece to Part: One to Many Relationship
Student to Piece: Many to Many Relationship

Refer to the diagram below for a visual representation of the table relationships:

[Table Relationship Diagram](file:///Users/donaldhull/Development/Code/Phase-3/phase-3-project/Phase%203%20Project%20Diagram.png)

## Resources

I implemented one external library for CLI fonts/formatting - PyFiglet!

To learn more about PyFiglet, click here: [PyFiglet](https://pypi.org/project/pyfiglet/)