#!/usr/bin/python3
"""
This script fetches tasks associated with a given employee ID and
exports them to a JSON file formatted as required.
"""

import json
import requests
import sys


def export_tasks_to_json(employee_id):
    """
    Fetches tasks for an employee and exports them to a JSON file
    """
    # API endpoints
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Make requests
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Prepare data for JSON export
    user_tasks = [{
        "task": todo["title"],
        "completed": todo["completed"],
        "username": user["username"]
    } for todo in todos]

    # Dictionary with user ID as key
    tasks_dict = {employee_id: user_tasks}

    # Write to JSON file
    with open(f"{employee_id}.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_tasks_to_json(sys.argv[1])
