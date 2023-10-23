#!/usr/bin/python3
'''extend your Python script to export data in the JSON format.'''
import json
import requests
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py \"employee id\"")
        exit(1)

    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w", newline="") as json_file:
        json.dump({id: [{
            "task": n.get("title"),
            "completed": n.get("completed"),
            "username": username
        } for n in todo]}, json_file)
