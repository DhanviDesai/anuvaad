import config
import json
from models import UserAuthenticationModel


class UserAuthenticationRepositories:

    @staticmethod
    def user_login(userName, password):

        result = UserAuthenticationModel.user_login(userName, password)

        return result

    @staticmethod
    def user_logout(userName):

        result = UserAuthenticationModel.user_logout(userName)

        return result

    @staticmethod
    def token_search(token):

        result = UserAuthenticationModel.token_search(token)

        return result
