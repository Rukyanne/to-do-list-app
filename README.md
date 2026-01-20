#  To-Do List Command Line Application

A simple, persistent command-line interface (CLI) application built with Python to help you manage your personal tasks efficiently. This project demonstrates core programming concepts and follows the Software Development Life Cycle (SDLC) methodology.

---

##  Student Information

- **Name:** Etohwo Annabelle Rukevwe
- **Department:** Computer Science
- **Matric Number:** 24/13958
- **Repository URL:** [https://github.com/Rukyanne/to-do-list-app](https://github.com/Rukyanne/to-do-list-app)

---


##  Features

The application provides the following functionality:

-  **Add Tasks** - Quickly create new tasks with descriptions
-  **View Tasks** - Display all tasks with their current status
-  **Mark Complete** - Change task status from pending `[ ]` to complete `[X]`
-  **Delete Tasks** - Permanently remove tasks from your list
-  **Data Persistence** - Tasks automatically save to `tasks.txt` between sessions
-  **Simple Interface** - Easy-to-use menu-driven command line interface
-  **Session Continuity** - Your tasks are preserved even after closing the application

---

##  Demo

### Application in Action

When you run the application, you'll see an interactive menu like this:

```
========================================
        TO-DO LIST MANAGER
========================================
1. View all tasks
2. Add a new task
3. Mark task as complete
4. Delete a task
5. Exit
========================================
Enter your choice (1-5): 
```

**Example workflow:**
1. Add tasks to your list
2. View them with completion status
3. Mark important tasks as complete
4. Remove finished or unwanted tasks
5. Exit knowing your data is saved

---

##  Prerequisites

Before running this application, ensure you have:

- **Python 3.x** installed on your system
  - [Download Python](https://www.python.org/downloads/)
  - Verify installation: `python --version` or `python3 --version`
- A **terminal/command prompt** application
- A **text editor** or IDE (VS Code, PyCharm, etc.) - optional but recommended
- **Git** for version control (optional)

### System Requirements
- **Operating System:** Windows, macOS, or Linux
- **Disk Space:** < 1 MB
- **Python Version:** 3.6 or higher

---

##  Installation

Follow these steps to set up the project on your local machine:

### Method 1: Clone the Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/Rukyanne/to-do-list-app.git

# Navigate to the project directory
cd to-do-list-app

# Verify files are present
ls  # On Windows use: dir
```

### Method 2: Download ZIP

1. Go to the [repository page](https://github.com/Rukyanne/to-do-list-app)
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract the ZIP file to your desired location
5. Navigate to the extracted folder in your terminal

---

##  How to Use

### Starting the Application

1. **Open your terminal/command prompt**

2. **Navigate to the project folder:**
   ```bash
   cd path/to/to-do-list-app
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```
   
   *If the above doesn't work, try:*
   ```bash
   python3 main.py
   ```

### Using the Menu Options

Once the application starts, you'll see a menu with 5 options:

#### **Option 1: View All Tasks**
- Displays all tasks in your list
- Shows task numbers, descriptions, and completion status


#### **Option 2: Add a New Task**
- Prompts you to enter a task description
- Task is added to your list as "pending" (uncompleted)
- Automatically saves to file

**Example:**
```
Enter task description: Study for Computer Science exam
Task added successfully!
```

#### **Option 3: Mark Task as Complete**
- View your current tasks
- Enter the task number you want to mark as complete
- Status changes from `[ ]` to `[X]`

**Example:**
```
Enter task number to mark as complete: 1
Task marked as complete!
```

#### **Option 4: Delete a Task**
- View your current tasks
- Enter the task number you want to delete
- Task is permanently removed from the list

**Example:**
```
Enter task number to delete: 2
Task deleted successfully!
```

#### **Option 5: Exit**
- Saves all tasks and closes the application
- Your data remains in `tasks.txt` for next time

---

##  Sample Output

Here's what you'll see when using the application:

### First Run (No Tasks)
```
========================================
        TO-DO LIST MANAGER
========================================
1. View all tasks
2. Add a new task
3. Mark task as complete
4. Delete a task
5. Exit
========================================
Enter your choice (1-5): 1

Your task list is empty!
```

### Adding Tasks
```
Enter your choice (1-5): 2
Enter task description: Complete Python assignment
Task added successfully!

Enter your choice (1-5): 2
Enter task description: Read Chapter 5 of textbook
Task added successfully!

Enter your choice (1-5): 2
Enter task description: Practice coding exercises
Task added successfully!
```

### Viewing Tasks
```
Enter your choice (1-5): 1

========================================
           YOUR TASKS
========================================
1. [ ] Complete Python assignment
2. [ ] Read Chapter 5 of textbook
3. [ ] Practice coding exercises
========================================
Total tasks: 3 | Completed: 0
========================================
```

### Marking Task as Complete
```
Enter your choice (1-5): 3
Enter task number to mark as complete: 1
Task marked as complete!

Enter your choice (1-5): 1

========================================
           YOUR TASKS
========================================
1. [X] Complete Python assignment
2. [ ] Read Chapter 5 of textbook
3. [ ] Practice coding exercises
========================================
Total tasks: 3 | Completed: 1
========================================
```

### Deleting a Task
```
Enter your choice (1-5): 4
Enter task number to delete: 2
Task deleted successfully!

Enter your choice (1-5): 1

========================================
           YOUR TASKS
========================================
1. [X] Complete Python assignment
2. [ ] Practice coding exercises
========================================
Total tasks: 2 | Completed: 1
========================================
```

---

##  Code Structure

### Project Files

```
to-do-list-app/
│
├── main.py           # Main application file with all logic
├── tasks.txt         # Data file (auto-created on first run)
├── .gitignore        # Git ignore rules
└── README.md         # This documentation file
```

### Key Components in `main.py`

```python
# 1. Data Persistence Functions
load_tasks()          # Reads tasks from tasks.txt
save_tasks()          # Writes tasks to tasks.txt

# 2. Core Features
add_task()            # Adds new task to list
view_tasks()          # Displays all tasks with status
mark_complete()       # Changes task status to complete
delete_task()         # Removes task from list

# 3. User Interface
display_menu()        # Shows menu options
main()                # Main program loop
```

### How Data is Stored

Tasks are stored in `tasks.txt` with a simple format:
```
[ ] Buy groceries
[X] Complete homework
[ ] Call dentist
```

- `[ ]` indicates an incomplete task
- `[X]` indicates a completed task
- Each line represents one task

---

##  SDLC Development History

This project followed the **Waterfall SDLC** model with clear phases:

### Phase 1: Requirements Analysis (TODO-001)
- **Objective:** Define project scope and requirements
- **Deliverables:** 
  - List of required features
  - User stories and use cases
  - Functional specifications
- **Features Defined:**
  - Add tasks
  - View tasks
  - Mark tasks complete
  - Delete tasks
  - Persistent storage

### Phase 2: Design
- **Objective:** Plan the application architecture
- **Decisions Made:**
  - Command-line interface for simplicity
  - Text file storage for persistence
  - Menu-driven user interaction
  - Simple task status representation

### Phase 3: Implementation (TODO-002)
- **Objective:** Build core functionality
- **Completed:**
  - File I/O operations (load/save)
  - View tasks functionality
  - Add task functionality
  - Basic menu system
- **Technologies:** Python 3, file handling

### Phase 4: Testing & Finalization (TODO-003)
- **Objective:** Complete remaining features and test
- **Completed:**
  - Mark complete functionality
  - Delete task functionality
  - Error handling
  - Edge case testing
  - User acceptance testing
- **Result:** All requirements met and verified

### Lessons from Waterfall Approach
-  Clear documentation at each phase
-  Structured development process
-  Easy to track progress against requirements
-  Limited flexibility for requirement changes
-  Good for learning and small projects

---



##  What I Learned

Through building this project, I gained practical experience with:

### Python Programming Concepts
-  **Functions:** Creating reusable code blocks
-  **Lists:** Managing collections of data
-  **File I/O:** Reading from and writing to files
-  **String Manipulation:** Working with text data
-  **Loops:** While loops for menu systems
-  **Conditionals:** If/elif/else statements for decision making
-  **Error Handling:** Try/except blocks for robust code

### Software Development Skills
-  **SDLC Process:** Following structured development methodology
-  **Requirements Analysis:** Defining project scope
-  **Version Control:** Using Git and GitHub
-  **Documentation:** Writing clear README files
-  **Testing:** Verifying functionality works as expected
-  **Problem Solving:** Debugging and fixing issues

### Real-World Application
-  **Data Persistence:** Making data survive program restarts
-  **User Interface Design:** Creating intuitive menus
-  **Project Organization:** Structuring code effectively
-  **Best Practices:** Using .gitignore, comments, and clean code

---

