import json
from json import JSONDecodeError
import os
from app.exception import EmailExistError

FILEPATH = os.getenv("FILEPATH")


def read_json(filepath: str) -> list:

    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)

    except JSONDecodeError:
        with open(filepath, "w") as json_file:
            json.dump({"data": []}, json_file)
        return {"data": []}

    except FileNotFoundError:
        os.mknod(filepath)

        with open(filepath, "w") as json_file:
            json.dump({"data": []}, json_file)
        return {"data": []}


def write_json(filepath: str, payload: dict):

    try:
        json_list = read_json(filepath)
        json_list["data"].append(payload)

        with open(filepath, "w") as json_file:
            json.dump(json_list, json_file, indent=2)
            return payload

    except FileNotFoundError:
        os.mknod(filepath)
        json_list = read_json(filepath)
        json_list["data"].append(payload)

        with open(filepath, "w") as json_file:
            json.dump(json_list, json_file, indent=2)
            return payload


def email_already_exist(email):
    data = read_json(FILEPATH)

    if len(data["data"]) > 0:
        for i in data["data"]:
            if email.lower() == i["email"]:
                raise EmailExistError


def check_is_upper(name, email):
    nameSplit = name.split(" ")
    result = ""

    for i in range(0, len(nameSplit)):
        result += str(nameSplit[i][0].upper()) + nameSplit[i][1:] + " "
    return (result[0:-1], email.lower())


def check_id():
    data = read_json(FILEPATH)
    result = 1

    if data["data"]:
        result = data["data"][-1]["id"] + 1

    return result
