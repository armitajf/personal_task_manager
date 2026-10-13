# Personal Task Manager
This program stores and manages user information.
## Table of contents



- [Project Title](#TProject-Title)
- [Description](#Description)
- [Table Of Contents](#Table-Of-Contents)
- [Features](#features)
- [Project Structure](#project-structure)
- [File Description](#File-Desciption)
- [Requirements](#requirments)
- [Installation](#installation)
- [Enviroment Setup](#envoirment-setup)
- [Usage](#usage)
- [Example Output](#exmaple-outout)
- [Screenshot](#screenshot)
- [Demo](#Demo)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licnse](#licnce)
- [Author](#author)



## Project Title
- **`Personal Task Manager`**

## Description
- The goal of this program is to collect and store user information, allowing the user to "manage all" of it .



## Features
- User Welcome
  - Asks the user for their name
  - Displays a welcome message
- Task Management
  - Collects tasks from the user
  - Stores tasks in a list
  - Displays all entered tasks
  - Stops collecting tasks when the user enters done
- Task Storage
  - Saves tasks in `tasks.txt`
  - Stores each task on a separate line
- Admin Mode
  - Asks the user if they want to open admin mode
  - Requests the admin password
  - Checks if the entered password is correct
  - Displays a message based on the password
- Environment Variables
  - Loads environment variables using `python-dotenv`
  - Reads the admin password from `.env`
  - Keeps the admin password outside the main Python file


## Project Structure
```text
personal_task_manager/
├── main.py
├── tasks.txt
├── .env.example
├── .gitignore
└── requirements.txt
```


## File Description
| File | Description |
| --- | --- |
| `main.py` | main file used to run the PERSONAL TASK MANAGER |
| `tasks.py` | contains the function used to collect tasks |
| `.env.example` | shows the envoirment |variaples needed by the project |
| `.gitignore` | tells git which files and folders shold not be tracked |
| `requirements.txt` | lists the external Python packages required by the project |
| `README.md` | contains the project documentation |
| `tasks.txt` | stors the tasks entered by the user |


## Requirements
Before running the project make sure you have:
- `python`
- `python-dotenv`

## Installation
1. Open a terminal in the project folder.
2. Check that python is installed:
```bash
python --version
```
3. Install -r requrements.txt
```bash
pip install -r requrements.txt
```

## Enviroment Setup
1. Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. Open the new `.env` file
3. Replace the example value with your own password
```text
TASK_MANAGER_ADMIN_PASSWORD=your_password_here
```
4. save the file.
> Do not commit your `.env` file because it may conntain praivate information

## Usage
1. Open a terminal in the project folder
2. Run the program:
```bash
python main.py
```
3. Choose `yes` or `no` for admin mode
4. If you choose `yes`, enter the password from your `.env` file
5. Enter your name
6. Enter your tasks one by one
7. Type done to finish enterning tasks
8. View your tasks in the terminal
9. Your result is saved in `results.txt`


## Example Output
```text
1. do u want to open admin mode? yes/no: yes

2. enter admin password : 234
- wrong password

3. whats your name?armita
- welcome armita

4. please enter your task(if you don't want to enter any task enter (done)) : done
your task : 
-  done
```

## Screenshot

### start game
![start game](pictures\pic1.png)

### your task
![quiz](pictures\pic3.png)

### final 
![final score](pictures\pic2.png)


## Demo
![task manager demo](demo/Animation.gif)


## Roadmap

## Contributing

## Licnse

## Author/