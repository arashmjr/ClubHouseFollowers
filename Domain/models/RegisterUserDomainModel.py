import datetime


class RegisterUserDomainModel:

    email: str
    password: str
    creation_date: datetime
    answer_one: str
    answer_two: str
    answer_three: str

    def __init__(self, email: str, password: str, creation_date: datetime,
                 answer_one: str,
                 answer_two: str,
                 answer_three: str):

        self.email = email
        self.password = password
        self.creation_date = creation_date
        self.answer_one = answer_one
        self.answer_two = answer_two
        self.answer_three = answer_three

    def to_dict(self):
        return {"email": self.email,
                "password": self.password,
                "creation_date": self.creation_date,
                "answer_one": self.answer_one,
                "answer_two": self.answer_two,
                "answer_three": self.answer_three
                }

