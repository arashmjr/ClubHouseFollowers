from repository.UserFollowRepository import UserFollowRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.UserFollowDomainModel import UserFollowDomainModel


class UserFollowService:
    user_follow_repository: UserFollowRepository
    save_user_repository: SaveUserRepository

    def __init__(self, user_follow_repository: UserFollowRepository, save_user_repository: SaveUserRepository):

        self.user_follow_repository = user_follow_repository
        self.save_user_repository = save_user_repository

    def save_user_follow(self, json: str):

        model = UserFollowDomainModel(json['user_id'], json['follow_id'], json['order_id'])
        self.user_follow_repository.insert(model)
        document = self.save_user_repository.find_record_by_user_id(model.user_id)
        self.save_user_repository.update_coins(document)
        return True




