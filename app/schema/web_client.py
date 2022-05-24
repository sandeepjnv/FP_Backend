from flask_restplus import Namespace, fields

class WebClientAPIs:
    ins_namespace = Namespace('Web Client APIs')

    # ins_img_frame_request = ins_namespace.model('Image Frame',{
    #     'str_vehicle_id': fields.String(required=True, description='Vehicle ID'),
    #     'str_img_frame': fields.String(required=True, description='Image frame base64 encoded'),
    # })