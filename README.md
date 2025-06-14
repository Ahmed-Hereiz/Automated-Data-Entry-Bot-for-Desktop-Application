# Automated Data Entry Bot for Desktop Application

This project automates data entry into a desktop application (Notepad on Windows, nano on Linux) by fetching blog posts from the JSONPlaceholder API and typing them as text documents. It uses Python with the BotCity and PyAutoGUI libraries to simulate user interactions, meeting all requirements of the project specification. The main script `(main.py)` detects the operating system and runs the appropriate automation, with a primary focus on Windows for reliability and compatibility.

### How to Use the Project

This project is designed to be easy to set up and run. The `main.py` script automatically detects your operating system (Windows or Linux) and launches the appropriate automation script to perform the data entry task.

### Setup Instructions
#### 1 - Clone or Download the Project 
#### 2 - Create a Virtual Environment :
```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```
#### 3 - Install Dependencies:
```bash
pip install -r requirements.txt
```
#### 4 - Run `main.py` 
Execute the main script with an optional argument to specify the number of posts to process (default and max is 10):
```bash
python main.py --num-posts 10
```

## Requirements Fulfillment :
#### Setup:
- Python and a virtual environment are supported (see setup instructions).
- Required libraries (requests, pyautogui, botcity-framework-core) are installed via requirements.txt.
#### Automation Task:
- Uses `Notepad` (Windows) and `nano` (Linux) as the desktop applications.
- PyAutoGUI launches the application, types API-fetched blog posts (title and body), and saves files as post_{id}.txt in the output/ directory.
- Processes up to 10 posts in a loop.
- Data is sourced from the JSONPlaceholder API.
#### Error Handling:
- Handles application launch failures, API errors, and file-saving issues with graceful recovery (closes application and continues).
- Verifies file existence after saving to ensure success.
#### Cross-Platform:
- `main.py` detects the OS and runs the appropriate script, ensuring compatibility on Windows and Linux.
