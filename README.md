# Introduction

Users can load, execute, and modify instructions in a straightforward and interactive environment with the help of this application's virtual machine interface. Users can follow detailed instructions, view and modify memory values, and resume execution after halting.

# Installation Requirements

Ensure that you have the `getch` and `pytest` python modules installed `pip3 install getch` and `pip3 install pytest`
will work on most computers.

# Testing

Running tests is as simple at running `python3 -m pytest` not using `python3 -m` will not be able to find the src
module.

# Usage

First, and most importantly, you should **always** make sure that you begin in a terminal, or the application will not launch.

## Running Application

Typing `python3 -m src.main` will run the virtual machine and the app will begin. 

### Using Application

Once the application has opened, you will be met with the `Editor` window. Here you are able to open a file with instructions and edit as you like.
You may also save any changes, or save a new file by hitting the `Save` button. 

To run your instructions within the file:

Click on the `Running` tab to see your Output view on the left window, and the memory in the right window. 
To load a file into memory:

1. Click the `Open` button.
2. Select the file with the instructions you want to perform.

Now that the file has loaded, hit the `Run` button to begin instruction entry. 
To enter an instruction, click on the small input box underneath the left window. 

You may now begin typing your desired instructions.

# Screenshots

- [Running Tab](RunningTab.png)
- [Editor Tab](EditorTab.png)


# Links

- [Design Document](DESIGN.md)
- [Test Spreadsheet](https://docs.google.com/spreadsheets/d/1QTb8sKVDeXY4Bi7FBApc3YbCMB7P11IFhFzOigon37I/edit?usp=sharing)