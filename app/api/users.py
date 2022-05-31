from flask import request
from flask_restplus import Resource

# schema 
from app.schema import UserAPIs
# service
from app.service import login_user , signup_user

ins_namespace = UserAPIs.ins_namespace
ins_login_request = UserAPIs.ins_login_request



@ins_namespace.route('/signIn')
class Users(Resource):
    @ins_namespace.doc("Sign-in to Account")

    @ins_namespace.expect(ins_login_request,validate = True)
    @ins_namespace.response(201, 'Signed-in successfully')
    @ins_namespace.doc('Input credentials')
    def post(self):
        """Sign-in to Account""" 
        return login_user(request)

@ins_namespace.route('/signUp')
class Users(Resource):
    @ins_namespace.doc("Create new account")

    @ins_namespace.expect(ins_login_request,validate = True)
    @ins_namespace.response(201, 'Successfully created new account')
    @ins_namespace.doc('Input credentials')
    def post(self):
        """Create new account""" 
        return signup_user(request)
        