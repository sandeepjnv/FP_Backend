from flask import request
from flask_restplus import Resource

# schema 
from app.schema import ImageFrame
# service

ins_namespace = ImageFrame.ins_namespace
ins_img_frame_request = ImageFrame.ins_img_frame_request

@ins_namespace.route('/')
class ImageFrameAPI(Resource):
    @ins_namespace.doc("Base64 Encoded Image frame")

    @ins_namespace.expect(ins_img_frame_request,validate = True)
    @ins_namespace.response(201, 'Image frame saved')
    @ins_namespace.doc('Upload new image frame')
    def post(self):
        """Upload base64 encoded Image frame""" 
        return {"status":"success","message":""}