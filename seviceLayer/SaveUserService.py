from repository.SaveUserRepository import SaveUserRepository
from Domain.models.SaveUserDomainModel import SaveUserDomainModel


class SaveUserService:
    repository: SaveUserRepository

    def __init__(self, repository: SaveUserRepository):
        self.repository = repository

    def save_profile(self, json: str):
        model = SaveUserDomainModel(json['user_id'], json['name'], json['photo_url'], json['username'],
                                    json['token'], json['phone_number'], json['bio'], json['coin'])
        record = self.repository.find_record_by_user_id(model.user_id)

        if record is None:
            self.repository.insert(model)
            return True
        self.repository.remove_record(model.user_id)
        self.repository.insert(model)
        return True


