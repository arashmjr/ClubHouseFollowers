from repository.PackagesRepository import PackagesRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.GetPackagesDomainModel import GetPackagesDomainModel
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from flask import request
from flask import Request
import base64


class PackagesService:
    save_user_repository: SaveUserRepository
    packages_repository: PackagesRepository
    auth: AuthorizationManager

    def __init__(self, save_user_repository: SaveUserRepository, packages_repository: PackagesRepository,
                 auth: AuthorizationManager):
        self.packages_repository = packages_repository
        self.save_user_repository = save_user_repository
        self.auth = auth

    def get_packages(self, request: Request):
        list_pack = [{"package_id": 111, "package_name": "gold", "price": 150},
                     {"package_id": 222, "package_name": "silver", "price": 100},
                     {"package_id": 333, "package_name": "bronze", "price": 50}]

        packages = self.packages_repository.get_all()
        if packages == []:
            for item in list_pack:
                model = GetPackagesDomainModel(item['package_id'], item['package_name'], item['price'])
                self.packages_repository.insert(model)

        userID = self.auth.extract_user_id(request)

        #convert list to dict
        new_dict = {}
        for item in packages:
            item = item.pop('_id')  # remove and return the -id field to use as a key
            new_dict[item] = item
        print(new_dict)

        user = self.save_user_repository.find_record_by_user_id(userID)
        coin_user = user['coin']
        json = {'coin': coin_user, 'packages': packages}
        return json






