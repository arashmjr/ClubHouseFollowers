from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.SaveUserDomainModel import SaveUserDomainModel

class SaveUserService:
    repository: SaveUserRepository
    auth: AuthorizationManager


    def __init__(self, repository: SaveUserRepository, auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def save_profile(self, json:str):
        model = SaveUserDomainModel(json['user_id'], json['name'], json['photo_url'], json['username'],
                                    json['token'], json['phone_number'])
        record = self.repository.find_record_by_user_id(json['user_id'])
        if record is None:
            self.repository.insert(model)
            return True
        self.repository.remove_record(record)
        self.repository.insert(model)
        return True


