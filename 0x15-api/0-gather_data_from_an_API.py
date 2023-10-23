#!/usr/bin/python3
'''using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import requests
from sys import argv, exit


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py \"employee id\"")
        exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = [m.get("title") for m in todo if m.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(n)) for n in completed]
