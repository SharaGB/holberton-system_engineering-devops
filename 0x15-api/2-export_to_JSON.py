#!/usr/bin/python3
""" Export data in the JSON format. """
import json
from requests import get
from sys import argv

if __name__ == '__main__':
    USER_ID = int(argv[1])
    users = get('https://jsonplaceholder.typicode.com/users/{}'.
                format(USER_ID)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(USER_ID)).json()
    list = []
    for progress in todos:
        TASK_TITLE = progress.get('title')
        TASK_COMPLETED_STATUS = progress.get('completed')
        USERNAME = users.get('username')
        dict = {"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME}
        list.append(dict)
    print_dict = {USER_ID: list}
    with open(f'{USER_ID}.json', 'w') as f:
        json.dump(print_dict, f)
