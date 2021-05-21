from repository.UserFollowRepository import UserFollowRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.UserFollowDomainModel import UserFollowDomainModel
from Domain.models.SaveUserDomainModel import SaveUserDomainModel
from flask import jsonify

class UserFollowService:
    userfollow_repository: UserFollowRepository
    saveuser_repository: SaveUserRepository

    def __init__(self, userfollow_repository: UserFollowRepository, saveuser_repository: SaveUserRepository):

        self.userfollow_repository = userfollow_repository
        self.saveuser_repository = saveuser_repository


    def save_user_follow(self, json: str):
        model = UserFollowDomainModel(json['user_id'], json['follow_id'], json['order_id'])
        self.userfollow_repository.insert(model)

        document = self.saveuser_repository.find_record_by_user_id(model.user_id)
        # print(document)
        self.saveuser_repository.update_coins(document)
        # self.saveuser_repository.remove_all()
        # z = self.saveuser_repository.find()
        # print(z)
        return True




