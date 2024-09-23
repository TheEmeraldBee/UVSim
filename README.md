# Installation Requirements
Ensure that you have the `getch` python module installed `pip3 install getch` will work on most computers.
# Testing
Running tests is as simple at running `python -m pytest` not using `python -m` will not be able to find the src module.

# Running
First, and most importantly, you should **always** make sure that you are running in a terminal, or read events will not
function correctly.
## Running REPL
Typing `python -m src.repl` will run the repl. It will simulate your input in a vm without setting memory, allowing for
easy iterative testing and programming.

### Repl Commands
In order to debug your repl, the following commands allow for testing your program easily
- `memory` will list the memory in bullet points
- `accumulator` will print the current value of the accumulator
- `quit` will exit the repl, returning you to the shell
## Running Files
Typing `python -m src.main {filepath}` will run the virtual machine by loading the given filepath into memory.

# Unit Tests Spreadsheet
https://docs.google.com/spreadsheets/d/1QTb8sKVDeXY4Bi7FBApc3YbCMB7P11IFhFzOigon37I/edit?usp=sharing