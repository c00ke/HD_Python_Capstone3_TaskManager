# HD_Python_Capstone3_TaskManager
Task Manager 
This is a program for a small business that can help it to manage tasks assigne to each member of the team. 

The program works with two text files, user.txt and tasks.txt
tasks.txt store a list of all the tasks that the team is working on. The data for each task is stored on a seperate line in the text file. 
Each line contains the following data about a task in this order: 
1. The username of the person that the task is assigned to
2. The title of the task
3. A description of the task.
4. The date that the task was assigned to the user.
5. The Due date for the task
6. Either a Yes or a No value that specifies if the task has been completed yet. 

user.txt stores the username and password for each user that has permission to user your program
1. The format is username, password per line

The Program has a login menu, it displays an error message if the user enters a username that is not listed in the user.txt or enters a valid
username but not a password.
The user will be repeatedly asked for the username and password until they are correctr

A menu is displayed for the user to choose from once they are logged in
A different  menu is displayed for the admin

The admin will be able to register a new user, generate reports and display statistics as well as all the functions of the user
The reports generated will be written to two text files
One will contain details and statistics about tasks completed
The other will contain details and statistics about the users performance
When display statistics is chosen, these two text files will be displayed to the user

The user will be able to add tasks, view all tasks, view their own tasks
They will also be able to edit their own tasks or mark their task as complete (Yes/No)
The task will only be able to be edited if it has not yet been completed

