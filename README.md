 #### Video Demo:  <https://www.youtube.com/watch?v=hfJLbhbakng>
#### Description:

### Project : To-Do List App by [Mouad Ait Khouya]

- **GitHub Username**: [mouadsifaw]
- **edX Username**: [mouaduzumaki2001]
- **City and Country**: [VA], [USA]
- **Date**: [09-28-2024]

## Project Overview

The To-Do List Application is a simple yet effective tool designed to help users manage their daily tasks efficiently. This project allows users to add, view, and mark tasks as completed. Initially implemented as a command-line interface (CLI) program, the application is enhanced with a graphical user interface (GUI) using Python’s Tkinter library to improve usability and user experience.

## Project Structure

The project consists of three main files:

1. **`project.py`**: This file contains the main logic for the To-Do List application. It includes the main function that runs the app, along with three additional functions:
   - `add_task(task)`: This function takes a task as input and adds it to the task list.
   - `view_tasks()`: This function displays all tasks along with their completion status. It helps users see what they have on their plate.
   - `mark_task_completed(task_number)`: This function allows users to mark a specific task as completed by its number in the list.

   The main function handles user interactions, prompting them to select options to add, view, or complete tasks.

2. **`test_project.py`**: This file contains test cases for the main functions using the `pytest` framework. Testing is crucial in software development as it ensures that the code behaves as expected. Each function has corresponding tests that check various scenarios, such as adding tasks and marking them completed. This helps to catch any bugs early in the development process.

3. **`requirements.txt`**: This file lists the dependencies required to run the project. In this case, it includes `pytest` since it's used for testing the application. Having a requirements file makes it easy for others to install the necessary packages to run the project.


