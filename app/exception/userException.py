class NumError(Exception):
    def __init__(self, message=None, status_code=400):

        if message:
            self.message = message
        else:
            self.message = (
                "Proibida a entradas de números ou booleanos, favor não insistir"
            )
        self.status_code = status_code


class EmailExistError(Exception):
    def __init__(self, message=None, status_code=409):

        if message:
            self.message = message
        else:
            self.message = "E-mail já cadastrado"
        self.status_code = status_code
