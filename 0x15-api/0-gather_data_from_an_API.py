#!/usr/bin/python3
""" Using this REST API, for a given employee ID, returns
information about his/her TODO list progress. """
from requests import get
from sys import argv

if __name__ == '__main__':
    """ Returns information about his/her TODO list progress """
    id = int(argv[1])  # Is the employee ID
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(id)).json()
    users = get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)).json()

    if users and todos:
        EMPLOYEE_NAME = users.get('name')  # Name of the employee
        NUMBER_OF_DONE_TASKS = 0  # Number of completed tasks
        for tasks in todos:
            if tasks.get('completed') is True:
                # Total number of tasks
                NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(todos)
        # First line: Employee
        print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        # Second and N next lines display the title of completed tasks
        for tasks in todos:
            TASK_TITLE = tasks.get('title')
            if tasks.get('completed') is True:
                print(f"\t {TASK_TITLE}")
