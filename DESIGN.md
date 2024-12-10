# User Stories

- As a user I should be able to run my commands within a terminal.
- As a user I should be able to input a file and interact with my program.
- As a user I should be able to carry out each task in the application by following the directions step-by-step.
- As a user I should be able to halt the program's execution, preserve its state, and pick up where I left off at a later time.
- As a user I should be able to see the RAM status at any time while the program is running.
- As a user I should be able to manually change memory values while the program is running.
- As a user I should be able to run commands in the terminal and get prompt feedback each time.
- As a user I should be able to load the program from a file and have little delay in its launch.
- As a user I should be able to return the virtual machine to its original setup.
- As a user I should be able to interact with the program using a simple and intuitive graphical interface.

# Use Cases

1. User can read input into memory
2. User can branch to specific program location
3. User can load value from memory into the accumulator
4. User can store value in accumulator into memory
5. User can add memory at location to accumulator
6. User can subtract memory at location to accumulator
7. User can multiply memory at location to accumulator
8. User can divide memory at location to accumulator
9. User can branch to specific memory location if accumulator is 0
10. User can branch to specific memory location if accumulator is negative

# Functional Requirements

1. File Formats
    - The app must support two file formats; one for 4-digit files, and one for 6-digit files.
2. Dynamic Tabs
    - Users can open multiple tabs in the same application instance.
    - Each tab operates independently, allowing users to load, edit, and run separate files.
3. GUI Customization
    - Users can customize the primary and secondary colors of the GUI.
    - Changes can take effect immediately or require a restart.
4. Execution and Editing
    - Users can load and execute programs through the `Running` tab.
    - Users can edit programs in an `Editor` tab, with syntax validation before execution.
5. Memory Handling
    - The program must handle up to 250 lines of memeory and support 6-digit operations

# Non-Functional Requirements

1. Performance
    - The app should execute programs with minimal lag, even when handling the maximum memory size.
2. Usability
    - The GUI must be intuitive, with clearly labeled buttons and accessible customizatino options.
3. Persistence
    - User settings (like colors) must persist between sessions through a configuration file.
4. Cross-Platform
    - The app must run on Windows, macOS, and Linux without additional dependencies beyond Python.
5. Scalability
    - The app must handle future expansions, such as support for larger files.
