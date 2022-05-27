from flask_restplus import Namespace, fields

class RaspberryModuleAPIs:
    ins_namespace = Namespace('RaspberryPI module APIs')

    ins_img_frame_request = ins_namespace.model('Image Frame',{
        'str_vehicle_id': fields.String(required=True, description='Vehicle ID'),
        'str_img_frame': fields.String(required=True, description='Image frame base64 encoded'),
    })

    ins_location_update_request = ins_namespace.model('Location ',{
        'str_vehicle_id': fields.String(required=True, description='Vehicle ID'),
        'str_longitude': fields.String(required=True, description='Longitude'),
        'str_latitude': fields.String(required=True, description='Latitude'),
    })