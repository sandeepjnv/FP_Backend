from flask import request
from flask_restplus import Resource

# schema 
from app.schema import MobileClientAPIs
# service
from app.service import user_login

ins_namespace = MobileClientAPIs.ins_namespace
ins_mob_login_request = MobileClientAPIs.ins_mob_login_request

@ins_namespace.route('/search')
class ListAllvehicles(Resource):
    @ins_namespace.doc("List all vehicles")

    # @ins_namespace.expect(ins_img_frame_request,validate = True)
    @ins_namespace.response(201, 'List of all vehicles retrieved')
    @ins_namespace.doc('Input source and destination')
    def post(self):
        """List all vehicles""" 
        return {"status":"success","message":"success"}

@ins_namespace.route('/signIn')
class ListAllvehicles(Resource):
    @ins_namespace.doc("Sign-in to Account")

    @ins_namespace.expect(ins_mob_login_request,validate = True)
    @ins_namespace.response(201, 'Sign-in to Account')
    @ins_namespace.doc('Input credentials')
    def post(self):
        """Sign-in to Account""" 
        return user_login(request)
        