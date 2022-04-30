from flask import request
from flask_restplus import Resource

# schema 
from app.schema import RaspberryModuleAPIs
# service
from app.service import image_frame_to_seat_map

ins_namespace = RaspberryModuleAPIs.ins_namespace
ins_img_frame_request = RaspberryModuleAPIs.ins_img_frame_request

@ins_namespace.route('/image_frame')
class ImageFrame(Resource):
    @ins_namespace.doc("Base64 Encoded Image frame")

    @ins_namespace.expect(ins_img_frame_request,validate = True)
    @ins_namespace.response(201, 'Image frame saved')
    @ins_namespace.doc('Upload new image frame')
    def post(self):
        """Upload base64 encoded Image frame""" 
        return image_frame_to_seat_map(request)
        
@ins_namespace.route('/location')
class LocationUpdate(Resource):
    @ins_namespace.doc("Current GEO location")

    @ins_namespace.expect(ins_img_frame_request,validate = True)
    @ins_namespace.response(201, 'Location saved')
    @ins_namespace.doc('Update Current location')
    def post(self):
        """Update Current location""" 
        return image_frame_to_seat_map(request)