#!/usr/bin/python3
"""
This script fetches tasks associated with all employees from a given API
and exports them to a JSON file formatted as required.
"""
import json
import requests


def export_all_tasks_to_json():
    """
    Fetches tasks for all employees and exports them to a JSON
    file.
    """
    # API endpoints
    base_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(f'{base_url}/users').json()
    todos = requests.get(f'{base_url}/todos').json()

    # Organize tasks by user id
    user_tasks = {}
    for user in users:
        user_tasks[str(user['id'])] = [{
            "username": user['username'],
            "task": todo["title"],
            "completed": todo["completed"]
        } for todo in todos if todo['userId'] == user['id']]

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_tasks, jsonfile)


if __name__ == "__main__":
    export_all_tasks_to_json()
