#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    tasks = {EMPLOYEE_ID: []}

    for task in data:
        tasks[EMPLOYEE_ID].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        })

    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump(tasks, file)
