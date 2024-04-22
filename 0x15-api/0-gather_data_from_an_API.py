#!/usr/bin/python3
"""
A script that fetches information about an employee's TODO list
progress using the JSONPlaceholder API.
"""

import requests
import sys


def fetch_todo_list(employee_id):
    """Fetches and prints the TODO list progress of a given employee."""
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user details
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetch todos for the user
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Compute the number of completed tasks
    total_tasks = len(todos)
    completed_tasks = len([task for task in todos if task['completed']])

    # Print the employee's TODO list progress
    print(f"Employee {user['name']} is done with tasks("
          f"{completed_tasks}/{total_tasks}):")
    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_todo_list(sys.argv[1])
