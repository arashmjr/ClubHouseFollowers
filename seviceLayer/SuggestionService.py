from repository.UserFollowRepository import UserFollowRepository
from repository.SaveOrderRepository import SaveOrderRepository
from repository.SaveUserRepository import SaveUserRepository
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from flask import Request
from flask import request
import base64
import random


class SuggestionService:
    order_repository: SaveOrderRepository
    user_follow_repository: UserFollowRepository
    save_user_repository: SaveUserRepository
    auth: AuthorizationManager

    def __init__(self, order_repository: SaveOrderRepository, user_follow_repository: UserFollowRepository,
                 save_user_repository: SaveUserRepository, auth: AuthorizationManager):
        self.order_repository = order_repository
        self.user_follow_repository = user_follow_repository
        self.save_user_repository = save_user_repository
        self.auth = auth

    def suggestion_user(self, request: Request):
        list_users = self.order_repository.find_suggestions()

        #update isActive user's before GET
        for item in list_users:
            count = self.user_follow_repository.find_count_of_followIds(item['user_id'], item['order_id'])
            if count is not None:
                if count == item['size']:
                    document = self.order_repository.find_record_by_user_id(item['user_id'])
                    self.order_repository.update_isActive_field(document)

        # GET records in order's table that isActive True
        arr_users = []
        arr = self.order_repository.find_suggestions()
        for record in arr:
            if record['isActive'] == True:
                arr_users.append(record)

        # if request.headers.get('authorization') is None:
        #     return {'success': False}, 401
        # else:
        #     encode_token = request.headers['authorization']
        #     list_token = encode_token.split('.')
        #     second_part = list_token[1]
        #
        #     decode_second_part = base64.b64decode(str(second_part) + '==')
        #
        #     string = decode_second_part.decode("UTF-8")
        #
        #     # split from Left
        #     split_from_Left = string.split('"user_id":')
        #     userId_str = split_from_Left[1]
        #
        #     # split from right
        #     split_from_right = userId_str.split('}')
        #     userID = split_from_right[0]

        userID = self.auth.extract_user_id(request)
        final_orders = []
        for item in arr_users:
            record = self.user_follow_repository.find_record_by_followId_orderId(userID, item['user_id'], item['order_id'])
            spec_record = list(record)
            if spec_record == []:
                final_orders.append(item)



        final_suggestion = []
        for item in final_orders:
            document = self.save_user_repository.find_suggestions_order(item['user_id'])
            if document is not None:
                final_suggestion.append(document)

        # set the number to select here.
        num_to_select = 5
        list_of_random_items = random.sample(final_suggestion, num_to_select)

        # convert list to dict
        new_dict = {}
        for item in list_of_random_items:
            item = item.pop('_id')  # remove and return the -id field to use as a key
            new_dict[item] = item

        return list_of_random_items






























