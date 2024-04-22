#!/usr/bin/python3
"""
This script fetches information about an employee's TODO list
progress and exports it to a CSV file.
"""
import csv
import requests
import sys


def export_tasks_to_csv(employee_id):
    """
    Fetches employee's tasks and exports them to a CSV file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user['username'],
                task['completed'],
                task['title']
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_tasks_to_csv(sys.argv[1])
