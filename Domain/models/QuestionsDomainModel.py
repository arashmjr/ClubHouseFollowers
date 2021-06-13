class QuestionsDomainModel:

    question_one: str
    question_two: str
    question_three: str
    user_id_one: str
    user_id_two: str
    user_id_three: str

    def __init__(self, question_one: str, question_two: str, question_three: str,
                 user_id_one: str, user_id_two: str, user_id_three: str):

        self.question_one = question_one
        self.question_two = question_two
        self.question_three = question_three
        self.user_id_one = user_id_one
        self.user_id_two = user_id_two
        self.user_id_three = user_id_three

    def to_list(self):
        return [
            {"title": self.question_one, "id": self.user_id_one},
            {"title": self.question_two, "id": self.user_id_two},
            {"title": self.question_three, "id": self.user_id_three}
                ]

