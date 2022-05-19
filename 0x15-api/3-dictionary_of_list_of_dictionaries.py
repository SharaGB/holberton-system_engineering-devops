#!/usr/bin/python3
""" Export data in the JSON format. """
import json
from requests import get

if __name__ == '__main__':
    users = get('https://jsonplaceholder.typicode.com/users/').json()
    todos = get('https://jsonplaceholder.typicode.com/todos/').json()
    user_dict = {}
    name_dict = {}
    for tasks in users:
        USERNAME = tasks.get('username')
        USER_ID = tasks.get('id')
        user_dict[USER_ID] = []
        name_dict[USER_ID] = USERNAME

    for progress in todos:
        userId = progress.get('userId')
        USERNAME = name_dict.get(userId)
        TASK_TITLE = progress.get('title')
        TASK_COMPLETED_STATUS = progress.get('completed')
        dict = {"username": USERNAME, "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS}
        user_dict.get(userId).append(dict)
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
