#!/usr/bin/python3
""" Export data in the JSON format. """
import json
from requests import get

if __name__ == '__main__':
    users = get('https://jsonplaceholder.typicode.com/users/').json()
    todos = get('https://jsonplaceholder.typicode.com/todos/').json()
    data = {}
    for user in users:
        list_employees = []
        for progress in todos:
            USERNAME = user.get('username')
            TASK_TITLE = progress.get('title')
            TASK_COMPLETED_STATUS = progress.get('completed')
            list_employees.append({"username": USERNAME, "task": TASK_TITLE,
                                   "completed": TASK_COMPLETED_STATUS})
        data[user['id']] = list_employees

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
