from flask_restplus import Namespace, fields

class UserAPIs:
    ins_namespace = Namespace('User APIs')

    ins_login_request = ins_namespace.model('User',{
        'str_user_name': fields.String(required=True, description='Username'),
        'str_password': fields.String(required=True, description='Password'),
    })