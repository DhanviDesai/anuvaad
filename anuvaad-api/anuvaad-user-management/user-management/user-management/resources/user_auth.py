from flask_restful import fields, marshal_with, reqparse, Resource
from repositories import UserAuthenticationRepositories
from models import CustomResponse, Status
from utilities import UserUtils
from utilities import MODULE_CONTEXT
import ast
from anuvaad_auditor.loghandler import log_info, log_exception
from flask import request
from anuvaad_auditor.errorhandler import post_error


class UserLogin(Resource):

    def post(self):
        body = request.get_json()
        if "userName" not in body.keys():
            return post_error("Key error","userName not found",None), 400
        if "password" not in body.keys():
            return post_error("Key error","password not found",None), 400
        
        userName = body["userName"]
        password = body["password"]

        validity=UserUtils.validate_user_login_input(userName, password)
        log_info("User validation:{}".format(validity),MODULE_CONTEXT)
        if validity is not None:
                return validity, 400

        try:
            result = UserAuthenticationRepositories.user_login(
                userName, password)
            log_info("User logout result:{}".format(result),MODULE_CONTEXT)
            if result == False:
                res = CustomResponse(
                    Status.FAILURE_USR_LOGIN.value, None)
                return res.getresjson(), 400

            res = CustomResponse(Status.SUCCESS_USR_LOGIN.value, result)
            return res.getresjson(), 200
        except Exception as e:
            log_exception("Exception while  user login: " +
                      str(e), MODULE_CONTEXT, e)
            return post_error("Exception occurred", "Exception while performing user login", None), 400
            


class UserLogout(Resource):

    def post(self):
        body = request.get_json()
        if "userName" not in body.keys():
            return post_error("Key error","userName not found",None)
        userName = body["userName"]

        if not userName:
            res = CustomResponse(
                Status.ERR_GLOBAL_MISSING_PARAMETERS.value, None)
            return res.getresjson(), 400

        try:
            result = UserAuthenticationRepositories.user_logout(userName)
            log_info("User logout result:{}".format(result),MODULE_CONTEXT)
            if result == False:
                res = CustomResponse(
                    Status.FAILURE_USR_LOGOUT.value, None)
                return res.getresjson(), 400
            else:
                res = CustomResponse(Status.SUCCESS_USR_LOGOUT.value, None)
            return res.getres()
        except Exception as e:
            log_exception("Exception while logout: " +
                      str(e), MODULE_CONTEXT, e)
            return post_error("Exception occurred", "Exception while performing user creation", None), 400
            


class AuthTokenSearch(Resource):

    def post(self):
        body = request.get_json()
        if "token" not in body.keys():
            return post_error("Key error","token not found",None)
        token = body["token"]
        validity=UserUtils.token_validation(token)
        log_info("Token validation result:{}".format(validity),MODULE_CONTEXT)
        if validity is not None:
                return validity, 400

        try:
            result = UserAuthenticationRepositories.token_search(token)
            log_info("User auth token search result:{}".format(result),MODULE_CONTEXT)
            if result == False:
                res = CustomResponse(
                    Status.FAILURE_USR_TOKEN.value, None)
                return res.getresjson(), 400
            else:
                res = CustomResponse(Status.SUCCESS_USR_TOKEN.value, result)
            return res.getres()
        except Exception as e:
            log_exception("Exception while user auth search: " +
                      str(e), MODULE_CONTEXT, e)
            return post_error("Exception occurred", "Exception while performing user creation", None), 400
            