from flask_restplus import Namespace, fields

class UserAPIs:
    ins_namespace = Namespace('Client APIs')

    ins_login_request = ins_namespace.model('Mobile client',{
        'str_user_name': fields.String(required=True, description='Username'),
        'str_password': fields.String(required=True, description='Password'),
    })