from repository.SuggestionRepository import SuggestionRepository

class SuggestionService:
    repository: SuggestionRepository

    def __init__(self, repository: SuggestionRepository):
        self.repository = repository

    def suggetion_user(self):
        # self.repository.remove_record(user_id='1487526937')
        record2 = self.repository.find_suggestions()
        print(record2)
        return True


