import enum


class Status(enum.Enum):

    SUCCESS = {'ok': True, 'http': {'status': 200},
               'why': "Request successful"}
    FAILURE_GLOBAL_SYSTEM = {'ok': False, 'http': {'status': 500},
                             'why': 'Request failed,Internal Server Error'}

    SUCCESS_USR_CREATION = {'ok': True, 'http': {'status': 200},
                            'why': "New users were created successfully"}
    FAILURE_USR_CREATION = {'ok': True, 'http': {'status': 400},
                            'why': "On input errors causing failure in user account creation"}

    SUCCESS_USR_UPDATION = {'ok': True, 'http': {'status': 200},
                            'why': "users were updated successfully"}
    FAILURE_USR_UPDATION = {'ok': True, 'http': {'status': 400},
                            'why': "On input errors causing failure in user account updation"}

    SUCCESS_USR_SEARCH = {'ok': True, 'http': {'status': 200},
                          'why': "users were updated successfully"}
    FAILURE_USR_SEARCH = {'ok': True, 'http': {'status': 400},
                          'why': "On input errors causing failure in user account updation"}

    SUCCESS_USR_LOGIN = {'ok': True, 'http': {'status': 200},
                         'why': "Logged in successfully"}
    FAILURE_USR_LOGIN = {'ok': True, 'http': {'status': 400},
                         'why': "On input errors causing failure in user login"}

    SUCCESS_USR_LOGOUT = {'ok': True, 'http': {'status': 200},
                          'why': "Logged out successfully"}
    FAILURE_USR_LOGOUT = {'ok': True, 'http': {'status': 400},
                          'why': "On input errors causing failure in user logout"}

    SUCCESS_USR_TOKEN = {'ok': True, 'http': {'status': 200},
                         'why': "Search is successful"}
    FAILURE_USR_TOKEN = {'ok': True, 'http': {'status': 400},
                         'why': "On input errors causing failure in user search"}

    ERR_GLOBAL_SYSTEM = {'ok': False, 'http': {
        'status': 500}, 'why': "Internal Server Error"}
    ERR_GLOBAL_MISSING_PARAMETERS = {
        'ok': False, 'http': {'status': 400}, 'why': "Data Missing"}

    