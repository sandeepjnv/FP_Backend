from flask_restplus import Namespace, fields

class MobileClientAPIs:
    ins_namespace = Namespace('Mobile Client APIs')

    ins_mob_login_request = ins_namespace.model('Mobile client',{
        'str_user_name': fields.String(required=True, description='Username'),
        'str_password': fields.String(required=True, description='Password'),
    })