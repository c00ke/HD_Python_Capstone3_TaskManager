import datetime
from datetime import date
import sys
from collections import defaultdict 

# Level 1, Task 25 (Capstone 5 - task_manager)
# Estine van der Berg, 02 April 2020

# This program will help a small business manage tasks assigned to each member of the team

# Create a Login menu based on the usernames and passwords stored in the 'user.txt' file, Define the login username and login password functions
# Read the user.txt file and save the password and username seperately, keeping in mind there is a ", " after the username
# Store the usernames and passwords in to two different lists
def login_user():
    login_details_user = []
    with open('user.txt', 'r+') as user_file:

        for line in user_file:
            line = line.strip().split(", ")
            login_details_user.append(line[0])
            
        return(login_details_user)


def login_pass():
    login_details_pass = []
    with open('user.txt', 'r+') as user_file:

        for line in user_file:
            line = line.strip().split(", ")
            login_details_pass.append(line[1])

        return(login_details_pass)
    
# Defining functions
# Define a function to register a new user, ask for a new password and username, confirm the password and write the information to the user.txt file
# Make sure that only admin can add new users, and that a user can't add a new user that already exists, display an error message if they do
def reg_user():
    print("\nRegister New User")
    new_username = input("Please enter new username: ").lower()

    new_password =""
    conf_password= ""
    userlists = []

    with open('user.txt', 'r+') as user_file:
        for word in user_file:
            
            # Create a list for the user names
            word = word.split(",")

        # Loop through this list of names and check if what the user entered exits
        # If yes we keep them in a loop until the name is unique
        while new_username in userlists:
                print("Username already exists")
                new_username = input("Please enter new username: ").lower()

        if new_username not in userlists :      
            new_password = input("Please enter new user's password: ")
            conf_password = input("Please confirm password: ")

    with open('user.txt', 'a') as user_file:

        # If new password is equal to old password, write details to file
        if (new_password == conf_password):
            new_user = ("\n"+new_username + ", " + new_password)
            user_file.write(new_user)


# Define function for user to add task - ask for the username of the person who the task will be assigned to, title, description and due date of task
# Date on which task is assigned is current date, and always assume task has not been completed
# Write new information to task_file
def add_task():
    with open('tasks.txt', 'a') as task_file:

        print("\nInput New Task")
        task_user = input("Assign a username to this task: ").lower()
        task_title = input("Enter the title of this task: ")
        task_descr = input("Please describe the task: ")
        task_due = input("Enter due date (01 January 2000): ")
        today = date.today()
        date_added = today.strftime("%d %B %Y")
        task_done = "No"
        task_info = (task_user + ", " + task_title + ", " + task_descr + ", " + date_added + ", " + task_due + ", " + task_done + "\n")
        task_file.write(task_info)


# Create a function to view all tasks - open the task_file again to extract info from it, display all the data from task.txt file
def view_all():
    task_num = 0

    # Open your tasks file, loop through the file and for each line add 1 to your variable created above
    with open ('tasks.txt', 'r+') as task_file:
        for line in task_file:
            line = line.strip().split(", ")
            task_num +=1

            # Print all the tasks in a readable manner
            display_view_all = ("\nTask: " + str(task_num) +
                                "\nTask name: " + line[1] +
                                "\nAssigned to: " + line[0] +
                                "\nTask Description: " + line[2] +
                                "\nDate assigned: " + line[3] +
                                "\nDue date: " + line[4] +
                                "\nTask Complete: " + line[5])
            print(display_view_all)

# Define a function where you find the username of person currently logged in and display their tasks assigned to them
def view_mine():

    # Call the list you created with all of your tasks
    tasks = load_tasks()
    
    # Define a variable that will increase with each iteration and become the task number
    task_num = 0

    
    for i in tasks:
        task_num +=1

        # If your list starts with the person loggedin, strip and split that line and output it for them in a easy to read manner
        if i.startswith(username):
            i = i.strip().split(", ")
            print("\nTask: " + str(task_num) +
                  "\nAssigned to: " + i[0] +
                  "\nTask name: " + i[1] +
                  "\nTask Description: " + i[2] +
                  "\nDate assigned:  " + i[3] +
                  "\nDue date: " + i[4] +
                  "\nTask Complete? " + i[5])

# Define a function that will mark your task as complete
def edit_my_task_comp():
    
    # Get input from user on which tasks they would like to edit
    edit_task_num = int(input("\nPlease choose a task you would like to edit (1, 2..)"
                              "\nElse to exit to main menu, please enter (-1): "))
    
    # Index will be task number minus 1
    index = (edit_task_num - 1)
    
    # If the user doesn't exit, Ask them if they would like to edit the document, or if they would like to mark it as complete, else return to main menu
    if edit_task_num != -1:
        edittask_user = input("\nPlease select 'Edit Task' (E) or 'Mark Task as Complete' (C). (E or C): ").upper()
    else:
        return
    
    # If user chooses to mark task as complete, open task file and read each line of task file. 
    if edittask_user == "C":  
        with open('tasks.txt', 'r+') as task_file:
            read_tasks = task_file.readlines()
        
            # Find the line we need to edit by using the index created (input from user -1) and split and strip this line. 
            edit_comp = (read_tasks[index])
            edit_comp = edit_comp.strip().split(', ')

            # If the task has not been completed, mark it as completed by removing the 'No' from the list created by readlines and adding on the 'yes'
            if edit_comp[5] == "No":
                edit_comp[5] = "Yes"
                
                # Create the new sentence that will be written to  your task file
                completed_task = (edit_comp[0] + ", " + edit_comp[1] + ", " + edit_comp[2] + ", " + edit_comp[3] + ", " + edit_comp[4] + ", " + edit_comp[5] +"\n")

                # Open your task file so that it can be written to, find the line you need to replace using indexing and rewrite the new sentence. Close your file
                f = open('tasks.txt', 'w')
                read_tasks[index] = completed_task
                f.writelines(read_tasks)
                f.close()
                print("Task has been marked as complete")

            # Else let the user know that the task has already been completed
            else:
                print("This task has been completed")
                
    # If user chooses to edit task, check if task has been completed, if Yes, the user will not be able to edit it. If No allow user to edit
    if edittask_user == "E":
    
    # First check if task is complete, if yes, user can't edit. If no, user can edit
        with open('tasks.txt', 'r+') as task_file:
            read_tasks = task_file.readlines() 
            edit_comp = (read_tasks[index])
            edit_comp = edit_comp.strip().split(', ')

            # If no, let the user decide what the will be doing, edit the username or the due date   
            if edit_comp[-1] == "No":
                print("\nEdit Task " + str(edit_task_num))
                username_duedate = input("Please select 'Edit Username' (A) or 'Due Date' (B). (A or B): ").upper()

                # If the user chooses the username, display the available usernames to them and ask them which user they would like to reassign to
                if username_duedate == "A":
                    print(login_details_user)
                    change = input("Which user would you like to assign this task to: ")
                    edit_comp[0] = change

                    # Create a new line that will be written to the task file
                    new_sentence = (edit_comp[0] + ", " + edit_comp[1] + ", " + edit_comp[2] + ", " + edit_comp[3] + ", " + edit_comp[4] + ", " + edit_comp[5] +"\n")

                    # Write new line to tasks text file
                    f = open('tasks.txt', 'w')
                    read_tasks[index] = new_sentence
                    f.writelines(read_tasks)
                    f.close()

                # If user decides to change the due date, ask them to input the new due date       
                elif username_duedate == "B":
                    change = input("Please enter new due date (01 January 2000): ")
                    edit_comp[4] = change

                    # Create a new line that will be written to the task file
                    new_sentence = (edit_comp[0] + ", " + edit_comp[1] + ", " + edit_comp[2] + ", " + edit_comp[3] + ", " + edit_comp[4] + ", " + edit_comp[5] +"\n")

                    # Write new line to task file
                    f = open('tasks.txt', 'w')
                    read_tasks[index] = new_sentence
                    f.writelines(read_tasks)
                    f.close()
                    
            # If the task has already been completed, let the user know       
            else:
                print("This task has already been completed and can not be edited")
         
# Define a function where you create a list with all of the information in your task file
def load_tasks():
    tasks = []
    index = 0

    # Loop through your task file, for every line there is a task, so for every line in the task file, append it to a list
    with open('tasks.txt', 'r+') as task_file:
        for line in task_file.readlines():
            line = line.strip()
            tasks.append(line)

        return(tasks)

# Define a function that work out total tasks/users created
def calc_file_total(filename):
    total = 0
    
    # Each new task is on a new line/each new user is on a new line, therefore, loop through chosen file and for each iteration add one to your total variable
    with open(filename, 'r+') as total_file:
        for line in total_file:
            total += 1

        return(total) 

# Define a function that works out all of the tasks that hav been completed
# Add yes or no to parameters to find completed or incompleted tasks
def completed_tasks(a):
    total = 0

    # Loop through task file, strip and split the lines into single strings. If string 5 = Yes/No add 1 to the total for each of them
    with open('tasks.txt', 'r+') as tasks_file:
        for line in tasks_file:
            line = line.strip().split(", ")
            if line[5] == a:
                total +=1

        return(total)
    
# Define a function that will find all the overdue files that are not complete
# Read all the lines where the due date is in the past or today, if it's true and Task is not completed, it's overdue
def overdue_tasks():
    overdue_task = 0

    # Loop through the tasks file, strip and split the lines, index 4 on each line is the current due date. 
    with open('tasks.txt', 'r+') as tasks_file:
        for line in tasks_file:
            line = line.strip().split(", ")
            due_date = line[4]
            duedate_object = datetime.datetime.strptime(due_date, "%d %B %Y")
            present = datetime.datetime.today()

            # If the current due date is in the past the task is overdue, for each iteration and overdue task in a line add one to ovedue tasks variable
            if (present >= duedate_object) and (line[5] == "No"):
                overdue_task += 1
        
        return(overdue_task)

# Define a function that will work out the % tasks that are incomplete
# Call the total tasks/users function and the total not completed tasks function to work out the percentage
def perc_incomp():
    total_tasks = calc_file_total('tasks.txt')
    not_compl = completed_tasks("No")
    
    not_compl_perc = ((not_compl/total_tasks)*100)

    return(not_compl_perc)


# Define a function that will work out the percentage of tasks that have are overdue
# Call the total tasks/users function and the total overdue tasks function to work out the percentage
def perc_overdue():
    total_tasks = calc_file_total('tasks.txt')
    tasks_overdue = overdue_tasks()
    
    overdue_perc = ((tasks_overdue/total_tasks)*100)
    overdue_perc = round(overdue_perc, 2)
    
    return(overdue_perc)

# Define a function to display all information and statistics from tasks folder in a report
# Calling all functions that were used to calculate this information
def task_overview():
        total_tasks = calc_file_total('tasks.txt')
        all_complete_tasks = completed_tasks("Yes")
        all_incomp_tasks = completed_tasks("No")
        total_overdue_tasks = overdue_tasks()
        perc_incomp_tasks = perc_incomp()
        perc_overdue_tasks = perc_overdue()
        today_date = date.today()

        # Display this information in a readable manner, and write it to a new file
        task_overview_display = ("\nReport: Tasks Overview" +
                                 "" +
                                 "\nReport generation date: " + str(today_date) +
                                 "\nTotal number of tasks: " + str(total_tasks) +
                                 "\nTotal completed tasks: " + str(all_complete_tasks) +
                                 "\nTotal incomplete tasks: " + str(all_incomp_tasks) +
                                 "\nTotal overdue tasks: " + str(total_overdue_tasks) +
                                 "\nPercentage of incomplete tasks: " + str(perc_incomp_tasks) + "%"+
                                 "\nPercentage of overdue tasks: " + str(perc_overdue_tasks)+ "%"
                                 )

        # Write to task overview file
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write(task_overview_display)                               
        
        return(task_overview_display)

# Define a function to work out total tasks assigned to each user:
# Call the username list function
# Loop through the task file, for each username in the username list
# Create a dictionary with the usernames as the keys and the amount of tasks per user as the value        
def total_tasks_per_user():
    list_of_users = login_user()
    per_user_total_tasks = defaultdict(int)
    
    with open ('tasks.txt', 'r+') as task_file:
        for line in task_file:
            line = line.strip().split(", ")
            
            for user in list_of_users:
                if user == line[0]:
                    per_user_total_tasks[user] += 1
    
    return(per_user_total_tasks)

# Define a function where you are working out the total percentage of tasks assigned to each user
# Call your functions for total amount of tasks and your user list as well as the total tasks per user
# Create a new dictionary that will contain the percentages
def total_tasks_perc_PU():
    total_tasks = calc_file_total('tasks.txt')
    dictionary_user_totals = total_tasks_per_user()
    list_of_users = login_user()

    user_total_per_dict = defaultdict(float)

    # Loop through your dictionary with user totals
    for k, v in dictionary_user_totals.items():

        # Work out user to task ratio
        user_task_ratio = ((v/total_tasks)*100)

        # Round of your percentage to nearest 2 decimals
        user_task_ratio = round(user_task_ratio, 2)

        # Add your values to your new dictionary
        user_total_per_dict[k] = user_task_ratio

    return(user_total_per_dict)


# Create a function that will be able to work out the percentage of either completed or not completed of total assigned tasks to each user.
# Use the total Tasks per user function to work this out
def perc_incomp_compl_tasks_PU(a):

    # Calling total tasks per user and usernames list functions
    total_tasks_assigned = total_tasks_per_user()
    list_of_users = login_user()

    #Creating a new dictionary in order to calculate the percentages
    
    user_completed_tasks_DICT = defaultdict(int)

    # Loop through the task_file to see which tasks have either been completed or not completed, depending on "yes or No"
    
    with open('tasks.txt', 'r+') as task_file:
        for line in task_file:
            line = line.strip().split(", ")
            user = line[0]
            complete = line[5]
            
            if user in line:
                if complete == a:
                   user_completed_tasks_DICT[user] += 1

        # Work out the percentage with the values from the two dicts
        
        user_perc_completed_dict = {k: (user_completed_tasks_DICT[k] / total_tasks_assigned[k])*100 for k in total_tasks_assigned}

        return(user_perc_completed_dict)

# Define a function that will work out the overdue percentage of tasks assigned to each user
# Call the functions you will need - total tasks assigned and the list of users
# Work out the total amount of overdue tasks per user, then divide my total tasks assigned per user and times by 100
def overdue_task_perc_per_user():
    total_tasks_assigned = total_tasks_per_user()
    list_of_users = login_user()

    # Create a new dictionary with the amount of overdue tasks per person
    due_tasks_per_user_dict = defaultdict(int)

    # Open the tasks file and loop through it, split each line into seperate strings
    with open('tasks.txt', 'r+') as tasks_file:
        for line in tasks_file:
            line = line.strip().split(", ")
            due_date = line[4]
            duedate_object = datetime.datetime.strptime(due_date, "%d %B %Y")
            present = datetime.datetime.today()
            for user in list_of_users:

                # For each user, check if their tasks are overdue by checking if due date is bigger than or equal to today
                if user == line[0]:
                    if (present >= duedate_object) and (line[5] == "No"):
                        # Iterate each task that is overdue into new dictionary created above
                        due_tasks_per_user_dict[user] += 1
       
    # Work out the percentage of overdue tasks per user by using the values in the new dictionary you created and dividing them by the total amount of tasks per user
    due_perc_per_user = {k: (due_tasks_per_user_dict[k] / total_tasks_assigned[k])*100 for k in total_tasks_assigned}
    
    return(due_perc_per_user)
    
# Define a function to display all information and statistics from user folder in a report
# Calling all functions that were used to calculate this information, and displaying them in a more readable manner to be written to user_overview file
def user_overview():
    
        total_users = calc_file_total('user.txt')
        total_tasks = calc_file_total('tasks.txt') 
        total_tasks_user = total_tasks_per_user()
        
        total_tasks_user_display_var = ""
        for k, v in total_tasks_user.items():
             total_tasks_user_display_var += "\n{}:{}".format(k, v)
             
        perc_total_tasks = total_tasks_perc_PU()
        perc_total_tasks_display = ""
        for k, v in perc_total_tasks.items():
             perc_total_tasks_display += "\n{}:{}".format(k, v)
             
        complete_tasks = perc_incomp_compl_tasks_PU("Yes")
        complete_tasks_display = ""
        for k, v in complete_tasks.items():
             complete_tasks_display += "\n{}:{}".format(k, v)
             
        incompl_tasks = perc_incomp_compl_tasks_PU("No")
        incompl_tasks_display = ""
        for k, v in incompl_tasks.items():
             incompl_tasks_display += "\n{}:{}".format(k, v)
             
        overdue_tasks = overdue_task_perc_per_user()
        overdue_tasks_display = ""
        for k, v in overdue_tasks.items():
             overdue_tasks_display += "\n{}:{}".format(k, v)
             
        today_date = date.today()
        
        # Display this information in a readable manner, and write it to a new file
        user_overview_display = ("\nReport: Users Overview" +
                                 "\nReport generation date: " + str(today_date) +
                                 "\nTotal number of users: " + str(total_users) +
                                 "\nTotal number of tasks generated: " + str(total_tasks) +
                                 "\nTotal number of tasks assigned per user: " + str(total_tasks_user_display_var) +
                                 "\nPercentage of the total number of tasks have been assigned per user: " + str(perc_total_tasks_display) +
                                 "\nWhat percentage of the tasks assigned have been completed per user: " + str(complete_tasks_display) + 
                                 "\nWhat percentage of the tasks assigned must still be completed per user: " + str(incompl_tasks_display) +
                                 "\nWhat percentage of the tasks assigned have not yet been completed and are overdue per user: " + str(overdue_tasks_display))
        
        # Write to User_overview file
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write(user_overview_display)
            
        return(user_overview_display)

# Define a statistics function - display the total number of tasks and the total number of users
# Loop through both txt files and count the number of lines in each.
def view_stats():
    count_users = 0
    count_tasks = 0

    with open('task_overview.txt', 'r+') as task_file:
            for line in task_file:
                line = line.strip()
                print(line)

    with open('user_overview.txt', 'r+') as user_file:
         for line in user_file:
             line = line.strip()
             print(line)

# To start with, User is not logged in

logged_in = False

# Ask the user to log in
print("\nPlease Login:")

username = input("\nPlease enter username: " ).lower()
password = input("Please enter password: ")
    
# Check if username and password are correct, else display an error and request again until correct details have been input
while logged_in == False:

    # Check if the username and password exist in the arrays, check if password and username correspond
    user_login = login_user()
    user_pass = login_pass()

    if username in user_login and password in user_pass and (user_login.index(username) == user_pass.index(password)):
        logged_in = True  
    else:
        print("You have entered the incorrect details, please try again: ")
        username = input("\nPlease enter username: " ).lower()
        password = input("Please enter password: ")

# Show menu when correct login details have been entered, if admin is the user, they should have an option to display statistics, generate report
# Use a while loop, so while user is logged in, it will return to the menu
while logged_in == True:
    if username == "admin" and password == "adm1n":
        print("\nPlease select one of the following options: ")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("ds - view statistics")
        print("e - exit")
        menu_choice = input("What would you like to do: ").lower()
    else:
        print("\nPlease select one of the following options: ")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")
        menu_choice = input("What would you like to do: ").lower()
        
    # Action each choice made
    # If 'r' is chosen, register a new user, ask for a new password and username, confirm the password and write the information to the user.txt file
    # Make sure that only admin can add new users
    if menu_choice == "r":
        if username == "admin" and password == "adm1n":
            register_users = reg_user()
        else:
            print("\nOnly admin can register new users")

    # If 'a' is chosen, ask for the username of the person who the task will be assigned to, title, description and due date of task
    # Date on which task is assigned is current date, and always assume task has not been completed
    # Write new information to task_file
    elif menu_choice == "a":
        add_new_task = add_task()

    # If 'va' is chosen, open the task_file again to extract info from it, display all the data from task.txt file
    elif menu_choice == "va":
        view_all_tasks = view_all()

    # If 'vm' is chosen, only display tasks belonging to the user that is logged in
    # If the username is equal to the first word on the line in the txt file, print the entire line
    # Give the user an option to change their tasks (call edit tasks function)
    elif menu_choice == "vm":
        view_my_tasks = view_mine()
        edit_tasks = edit_my_task_comp()

    # If 'gr' is chosen, call the functions that will generate the two reports and let the user know that this has been done
    elif menu_choice == "gr":
        generate_task = task_overview()
        generate_user = user_overview()
        print("Report has been generated, please display statistics to view report")
     
    # If 'stat' is chosen, display the total number of tasks and the total number of users
    # Loop through both txt files and count the number of lines in each. 
    elif menu_choice == "ds":
        display = view_stats()

    # If "e" (exit) is chosen, Log the user out
    else:
        menu_choice == "e"
        logged_in = False
