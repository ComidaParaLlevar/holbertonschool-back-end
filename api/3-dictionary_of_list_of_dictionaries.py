#!/usr/bin/python3
"""Script to use a REST API for a given employee, to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{API_URL}/users").json()

    user_dict = {}
    for user in users:
        tasks = requests.get(f"{API_URL}/users/{user['id']}/todos").json()

        user_dict[user['id']] = [{
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        } for task in tasks]

    with open("todo_all_employees.json", "w") as file:
        json.dump(user_dict, file)
