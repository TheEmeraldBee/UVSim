# Table of Contents:
* Introduction
* User Stories & Use Cases
* Functional Specifications
* Class Diagram & GUI Wire Frame
* Unit Test Explanation
* User Manual
* Future Roadmap


# Introduction:
Users can load, execute, and modify instructions in a straightforward and interactive environment with the help of this application's virtual machine interface. Users can follow detailed instructions, view and modify memory values, and resume execution after halting.


# User stories & Use cases:


## User Stories


- As a user, I should be able to run my commands within a terminal.
- As a user, I should be able to input a file and interact with my program.
- As a user, I should be able to carry out each task in the application by following the directions step-by-step.
- As a user, I should be able to halt the program's execution, preserve its state, and pick up where I left off later.
- As a user, I should be able to see the RAM status at any time while the program is running.
- As a user, I should be able to manually change memory values while the program is running.
- As a user, I should be able to run commands in the terminal and get prompt feedback each time.
- As a use,r I should be able to load the program from a file and have little delay in its launch.
- As a user, I should be able to return the virtual machine to its original setup.
- As a user, I should be able to interact with the program using a simple and intuitive graphical interface.


## Use Cases


1. The user can read input into memory
2. User can branch to specific program location
3. The user can load value from memory into the accumulator
4. The user can store value in the accumulator in memory
5. The user can add memory at a location to the accumulator
6. The user can subtract memory at a location to the accumulator
7. User can multiply memory at location to accumulator
8. User can divide memory at location to accumulator
9. The user can branch to a specific memory location if the accumulator is 0
10. The user can branch to a specific memory location if the accumulator is negative


# Functional specifications (your final SRS requirements doc):
- Include all previous functionality listed.
- Expand the scope of your application so data files can contain 250 lines instead of 100 (and likewise your internal memory registers will now go from 000 to 249 to match).  Note that this change will require the support of three-digit memory addresses instead of two -- as a result this feature will create a "new" file format supported from this time forward that will contain six digit words instead of four.
- Some additional notes: you should not support more than 250 lines (even though the address space now supports up to 1000 lines in theory).  Any command that references a line # that's not between 000 and 249 will be judged invalid.  Make sure your application does not allow the loading or editing of a file (such as copying and pasting) to ever have more than 250 lines.
Since your new word size is six digits, make sure your application can handle six digit math operations correctly, with the same overflow handling that you did with four digits.
The function codes for each operation will not change: simply append a zero to the beginning of each functional code (i.e. 010 instead of 10 will represent a READ command here using this 6 digit format).

- Support a one-way "conversion" process feature somewhere in your app where you can take a 4-digit file and convert it to a six-digit form (with leading zeroes) and save it to a "new" file format for later loading and execution.  (You do not need to provide a way to convert 6-digit files to 4)
- Your application should allow multiple files to be opened in the application at once (you can decide on the implementation -- GUI tabs, sub-windows, or other options, but the client should be able to have multiple files open simultaneously within your app instance, with the ability to switch between, edit, and/or execute each of those files in any order within the app.  Running multiple instances of your app does not count here -- the requirement is one instance that can handle multiple files at once.)

- Complete the README by adding the missing sections (Introduction, Installation Instructions, Usage Examples, and so forth), making existing instructions more user friendly, including pictures to make the README more understandable, & providing links to other documents & resources in the README.

- Improve all Design Documents by fixing notation in the Class Diagram, expanding upon the wireframe for a more comprehensive look, adding User Stories, add a document for functional & non-functional requirements. 

- Improve error handling & input validation. 

# Class diagrams and GUI wireframes:


- [Class Definition Document](diagrams\Class Definition Document 2.0.png)

- [GUI Wireframe](diagrams\wireframe2.0.png)

# Unit Test Descriptions


**test_add_instruction**- Tests to make sure that addition is happening correctly, not only with a positive number but with a zero as well. (0+69 = 69 & 0+0 = 0)
**test_branch**- Tests to make sure that if an instruction is set as something, it actually equals what it was set to, that it fails if it does not equal what it is set to, it fails. 
**test_cpu**- Tests to make sure the CPU is functioning, that the CPU’s counter will stay at 99 if you attempt to go beyond 99, and that the CPU will not work if you attempt to access location 100. 
**test_division_instruction**-Tests to make sure that the division instruction functions (69/69 = 1 & 69/1 = 69)
**test_halt_instruction**- Tests to make sure that at the correct instruction, the InstructionEvent.Quit even will occur. 
**test_load_instruction**- Tests to make sure that when you load either a positive or negative number it will, in fact, load correctly.
**test_memory**- Tests to make sure that the length of the memory & that what you’ve set a value to be at any point in the memory is correct. Also check for if you can access below or above what the memory should be able to access.
**test_multiply_instruction**-Tests to make sure that multiplication occurs correctly (2 * 69 = 138 & 0 * 0 = 0). 
**test_parsed_instruction**- Tests to make sure that instructions can be parsed/split correctly (ex: +123007 -> 1 is the sign, 123 is the instruction, and 7 is the address). Then, it goes on to test invalid length, sign characters, operating codes, & addresses
**test_store_instruction**- Tests to make sure that you can store information properly, whether it is positive or negative. 
**test_subtract_instruction**- Tests to make sure that the subtraction instruction functions properly (69-69 = 0 & 0-0 = 0). 



# User Manual
## Installation Requirements

Ensure that you have the `getch` and `pytest` Python modules installed. You can use `pip3 install getch` and `pip3 install pytest` if you are unsure to ensure that you have both modules installed. This will work on most computers.

## Testing

Running tests is as simple as running `python3 -m pytest` not using `python3 -m` will not be able to find the src module.

## Usage

First, and most importantly, you should **always** make sure that you begin in a terminal, or the application will not launch.

### Running Application

Typing `python3 -m src.main` will run the virtual machine and the app will begin.

#### Using Application

Once the application has opened, you will be met with the `Editor` window. Here you are able to open a file with instructions and edit it as you like.
You may also save any changes, or save a new file by hitting the `Save` button.

To run your instructions within the file:

Click on the `Running` tab to see your Output view on the left window, and the memory in the right window.
To load a file into memory:

1. Click the `Open` button.
2. Select the file with the instructions you want to perform.

Now that the file has loaded, hit the `Run` button to begin instruction entry.
To enter an instruction, click on the small input box underneath the left window.

You may now begin typing your desired instructions.

## Screenshots

- [Running Tab](RunningTab.png)
- [Editor Tab](EditorTab.png)


### Links

- [Design Document](DESIGN.md)
- [Test Spreadsheet](https://docs.google.com/spreadsheets/d/1QTb8sKVDeXY4Bi7FBApc3YbCMB7P11IFhFzOigon37I/edit?usp=sharing)





# Future Roadmap
We plan to add web support so that we can reach a wider market by allowing people to utilize our software via the web instead of needing to have it installed on their computers this will be accomplished via adding web support. Similarly, we plan to add mobile support so that we can allow people the ease and convenience of using our software on their phones. We also plan to add multi-file program support that doesn’t require an additional tab to be opened each time so that it is easier to use our program when you need to utilize multiple different files. For additional ease of use, we’re planning to allow for extension support so that a user may have extensions that help them use our UVsimulator program and understand what is happening. We also plan to allow for integration with the VSCode Language Server to allow for help while coding. Finally, we also will add graphics instructions for game development and other GUI projects so that users may experiment with more complex instructions & end products in the UVSimulator. 
