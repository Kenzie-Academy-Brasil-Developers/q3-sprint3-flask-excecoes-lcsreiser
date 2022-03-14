from flask import Flask, jsonify, request
import os
from .services import (
    read_json,
    write_json,
    email_already_exist,
    check_is_upper,
    check_id,
)

from .exception import EmailExistError, NumError

FILEPATH = os.getenv("FILEPATH")

app = Flask(__name__)


@app.get("/user")
def getUser():
    data = read_json(FILEPATH)
    return jsonify(data), 200


@app.post("/user")
def postUser():
    try:
        data = request.get_json()
        name = data["name"]
        email = data["email"]

        if type(name) == str and type(email) == str:
            email_already_exist(email)
            result = check_is_upper(name, email)
            idUser = check_id()
            return write_json(
                FILEPATH, {"id": idUser, "name": result[0], "email": result[1]}
            )
        else:
            raise NumError
    except NumError as e:
        return {"error": e.message}, e.status_code
    except EmailExistError as e:
        return {"error": e.message}, e.status_code
