# Jumper

Tension so thick you can cut it with a knife! <i>Jumper</i> seems like a pretty
laid back game until it's not! The rules are simple. The jumper guesses letters,
one at a time. If the letter's not in the puzzle, the parachute loses a line.
Guessing continues until the puzzle is solved or, well, you know.

## Getting Started

---

Make sure you have Python 3.8.0 or newer installed and running on your machine.
Open a terminal and browse to the project's root folder. Start the program by
running the following command.

```
python3 jumper
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE
and open the project folder. Select the main module inside the hunter folder and
click the "run" icon.

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- game              (specific game classes)
    +-- __init__.py     (python package file)
    +-- console.py      (console class)
    +-- director.py     (director class/ control)
    +-- generate_words.py(word class)
    #NOTE: Copy the path of the wordlist.txt from your computer and change the path location in the generate_words.py. in order to detect the file. 
    +-- lives.py        (lives class)
    +-- puzzle.py       (puzzle class)
    +-- wordlist.txt    (list of words for the generate_words.py) 
    #NOTE: Copy the path of the wordlist.txt from your computer and change the path location in the generate_words.py. in order to detect the file. 
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```
#NOTE: Copy the path of the wordlist.txt from your computer and change the path location in the generate_words.py. in order to detect the file.
## Required Technologies

---

- Python 3.8.0

## Authors

---
Nicolas Paredes: par21035@byui.edu
Helama Barbour: Helamashi@gmail.com
James Charlie Salva: jamessalvajames@hotmail.com