import config
import json
from models import UserManagementModel


class UserManagementRepositories:

    @staticmethod
    def create_users(users):
        result = UserManagementModel.create_users(users)
        if result is not None:
            return result
        else:
            return True

    @staticmethod
    def update_users(users):
        result = UserManagementModel.update_users_by_uid(users)
        if result is not None:
            return result
        else:
            return True

    @staticmethod
    def search_users(userIDs, userNames, roleCodes):
        result = UserManagementModel.get_user_by_keys(
            userIDs, userNames, roleCodes)
        if result is not None:
            return result
        else:
            return ("No such users")