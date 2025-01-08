# Simple To-Do List Application

This repository contains a simple Python-based To-Do List application and a set of user stories. The goal is to practice creating unit tests that ensure each user story is properly addressed.

## Contents

- **`stories.txt`**  
  Contains user stories that describe the main features and expectations of the To-Do List application.

- **`app.py`**  
  Contains the Python code for the To-Do List application. This code includes intentional errors to encourage thorough testing.

- **`README.md`**  
  You’re reading it now. It explains how to create test cases based on the user stories and the application.

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

You should now see the following files (or similarly named ones) in the project folder:

- `stories.txt`
- `app.py`
- `README.md` (this file)

2. **Install Dependencies**

If you plan to run the application or write tests, you may need the following:

- **Python 3.7+** (or any later version).  
- **No additional libraries** are strictly required for the main application, since it only uses Python’s standard library.
- **Github Copilot VS Code Extension** can be found in the extensions marketplace. You'll need to be signed into a Github account to access the extension.
- **Optional**: If you plan to use a test framework such as `pytest`, install it:
  ```bash
  pip install pytest

- **Optional**: If you prefer the built-in `unittest` module, no extra steps are needed.

Make sure your system’s `python` or `python3` command refers to a compatible version, and that you have the necessary permissions to install packages.

3. **Review the Application and User Stories**

Before generating tests with GitHub Copilot, it’s important to understand what the application should do:

- **Open `stories.txt`**  
   - This file outlines the user stories that define the features of the To-Do List application.  
   - Each story details a requirement, such as adding tasks, listing tasks, marking them as completed, etc.

- **Examine the Python Code**  
   - Look at `app.py` (or the file name you’ve used).  
   - Study how each function implements (or attempts to implement) the features from the user stories.  
   - Note any bugs or quirks (e.g., the known bug in the `filter_tasks` function for pending tasks).

- **Gather Testing Ideas**  
   - As you read through both the user stories and the code, think about:
     - **Inputs** you’ll provide (e.g., task titles, IDs).  
     - **Outputs** or observable states (e.g., JSON contents, print statements).  
     - **Edge cases** (empty input, invalid IDs, etc.).  
   - Jot these down or keep them in mind so Copilot can help you generate meaningful tests.

## Creating Test Cases with GitHub Copilot

1. **Identify Features and Expected Behaviors**  
   - Read each user story in `stories.txt` and outline the expected behavior (inputs and outputs).
   - Think about edge cases (e.g., invalid task IDs, empty titles).

2. **Set Up a Test File**  
   - Create a new file (e.g., `test_app.py`).
   - You can use `pytest` or `unittest`; both are valid options.

3. **Use GitHub Copilot to Generate Test Stubs**  
   - Open `test_app.py` in an IDE with Copilot enabled.
   - Write a descriptive comment about the test you want, such as:
     ```python
     # Test that a new task can be added with the correct title, description, and status.
     def test_add_task():
         ...
     ```
     Copilot will suggest code to complete the test based on the context of your repository.

4. **Example of a Copilot-Generated Test**  
   ```python
   import os
   from app import add_task, load_tasks

   def test_add_task():
       # Clean up any existing data file before running the test
       if os.path.exists("tasks.json"):
           os.remove("tasks.json")

       # Add a new task
       add_task("Test Task", "This is a description")

       # Load tasks from the JSON file
       tasks = load_tasks()

       # Check that the task was added correctly
       assert len(tasks) == 1
       assert tasks[0]["title"] == "Test Task"
       assert tasks[0]["description"] == "This is a description"
       assert tasks[0]["completed"] == False
   ```

5. **Write Tests for Each User Story**  
   - **Story 1 (Add a Task)**: Ensure new tasks have the correct title, description, and default status (`completed = False`).  
   - **Story 2 (List Tasks)**: Check that `list_tasks()` outputs or returns the expected list of tasks.  
   - **Story 3 (Mark Task as Completed)**: Verify `mark_task_completed()` updates the task’s `completed` field.  
   - **Story 4 (Delete a Task)**: Ensure `delete_task()` removes the intended task.  
   - **Story 5 (Filter Tasks)**: Verify filtering for `completed` vs. `pending` tasks behaves as expected.

6. **Address the Intentional Error**  
   - The `filter_tasks` function has an intentional bug for "pending" tasks (`task["completed"] == True` instead of `False`).  
   - Write a test to confirm the correct behavior, observe the failure, then fix the bug in `app.py`.  
   - Re-run your tests to verify the fix resolves the issue.

## Running Your Tests

- Using `pytest`:
```python
pytest
```

- Using `unittest`
```python
python -m unittest discover
```

## Iteration and Best Practices

1. **Test Early, Test Often**  
   - Each time you add or change a feature, re-run your test suite to ensure everything still works as intended.

2. **Clean Up Test Data**  
   - The application writes to `tasks.json`. To avoid test conflicts, you may want to remove or back up this file before each test run.  
   - Alternatively, **mock** file operations for faster, more isolated tests.

3. **Let Copilot Assist, But Always Review**  
   - GitHub Copilot is a great helper, but make sure to review all generated test code.  
   - Ensure the tests reflect your true requirements and are not just boilerplate.

4. **Expand Features**  
   - After confirming these core features work correctly, consider adding new user stories (e.g., search, priority levels).  
   - Write new tests (with Copilot’s help) to cover those features as well.

5. **Collaboration and Feedback**  
   - If you’re working in a team, discuss your test strategy with teammates.  
   - Code review can catch mistakes that automated tests miss, and tests help ensure future code changes don’t introduce regressions.
