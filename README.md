# To-Do-List-App

## Features:

1. **Add Task:**
   - Enter a task in the provided field and click the "Add Task" button to add it to the list.
   - An error message will be displayed if the input field is empty.

2. **Delete Task:**
   - Select a task from the list and click the "Delete" button to remove it.
   - An error message will be displayed if no task is selected.

3. **Clear All Tasks:**
   - Click the "Clear All Tasks" button to delete all tasks in the list.
   - A confirmation dialog will be displayed before deleting all tasks.

4. **Exit:**
   - Click the "Exit" button to close the application.
   - All tasks will be saved to the database before exiting.

5. **Database Integration:**
   - Tasks are stored in an SQLite database (`listofTask.db`).
   - The application retrieves tasks from the database on startup and updates the database when tasks are added or deleted.

## Instructions:

1. Enter a task in the provided field and click "Add Task" to add it to the list.
2. Select a task from the list and click "Delete" to remove it.
3. Click "Clear All Tasks" to delete all tasks (confirmation required).
4. Click "Exit" to close the application.

## Requirements:

- Python 3.x
- Tkinter library (included in standard Python installation)
- SQLite library (included in standard Python installation)

## Known Issue:

- The delete key is not currently supported.To whom so ever it may concern i request to please help me out to make delete button work properly. Please use the "Clear all tasks" button to remove tasks.
