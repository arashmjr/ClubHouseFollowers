from repository.PackagesRepository import PackagesRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.GetPackagesDomainModel import GetPackagesDomainModel
from flask import request
import base64


class PackagesService:
    save_user_repository: SaveUserRepository
    packages_repository: PackagesRepository

    def __init__(self, save_user_repository: SaveUserRepository, packages_repository: PackagesRepository):
        self.packages_repository = packages_repository
        self.save_user_repository = save_user_repository

    def get_packages(self):
        list_pack = [{"package_id": 111, "package_name": "gold", "price": 150},
                     {"package_id": 222, "package_name": "silver", "price": 100},
                     {"package_id": 333, "package_name": "bronze", "price": 50}]

        packages = self.packages_repository.get_all()
        if packages == []:
            for item in list_pack:
                model = GetPackagesDomainModel(item['package_id'], item['package_name'], item['price'])
                self.packages_repository.insert(model)

        # x = self.packages_repository.get_all()
        # print(x)

        if request.headers.get('authorization') is None:
            return {'success': False}, 401
        else:
            encode_token = request.headers['authorization']
            list_token = encode_token.split('.')
            second_part = list_token[1]

            decode_second_part = base64.b64decode(str(second_part) + '==')

            string = decode_second_part.decode("UTF-8")

            # split from Left
            split_from_Left = string.split('"user_id":')
            userId_str = split_from_Left[1]

            # split from right
            split_from_right = userId_str.split('}')
            userID = split_from_right[0]

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






