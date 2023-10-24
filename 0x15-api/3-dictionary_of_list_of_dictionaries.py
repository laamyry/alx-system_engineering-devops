#!/usr/bin/python3
'''extend your Python script to export data in the JSON format.'''
import json
import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()

    with open("todo_all_employees.json", "w", newline="") as json_file:
        json.dump({m.get("id"): [{
            "task": n.get("title"),
            "completed": n.get("completed"),
            "username": m.get("username")
        } for n in todo if m.get("id") == n.get("userId")]
            for m in users}, json_file)
