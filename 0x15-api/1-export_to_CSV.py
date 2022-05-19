#!/usr/bin/python3
""" Extend your Python script to export data in the CSV format. """
import csv
from requests import get
from sys import argv

if __name__ == '__main__':
    USER_ID = int(argv[1])
    users = get('https://jsonplaceholder.typicode.com/users/{}'.
                format(USER_ID)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(USER_ID)).json()

    USERNAME = users.get('username')
    # Open the file in the write mode
    with open('{}.csv'.format(USER_ID), 'w') as f:
        # Create the csv writer
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for progress in todos:
            TASK_COMPLETED_STATUS = progress.get('completed')
            TASK_TITLE = progress.get('title')
            # Write a row to the csv file
            csv_writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
