from flask import request
from flask_restplus import Resource

# schema 
from app.schema import WebClientAPIs
# service

ins_namespace = WebClientAPIs.ins_namespace

@ins_namespace.route('/listVehicles')
class ListAllvehicles(Resource):
    @ins_namespace.doc("List all vehicles")

    # @ins_namespace.expect(ins_img_frame_request,validate = True)
    @ins_namespace.response(201, 'List of all vehicles retrieved')
    @ins_namespace.doc('Input source and destination')
    def post(self):
        """List all vehicles""" 
        return {"status":"success","message":"success"}
        