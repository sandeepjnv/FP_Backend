from flask import request
from flask_restplus import Resource

# schema 
from app.schema import UserAPIs
# service
from app.service import user_login

ins_namespace = UserAPIs.ins_namespace
ins_login_request = UserAPIs.ins_login_request



@ins_namespace.route('/signIn')
class Users(Resource):
    @ins_namespace.doc("Sign-in to Account")

    @ins_namespace.expect(ins_login_request,validate = True)
    @ins_namespace.response(201, 'Sign-in to Account')
    @ins_namespace.doc('Input credentials')
    def post(self):
        """Sign-in to Account""" 
        return user_login(request)
        