from flask_restplus import Namespace, fields

class VehicleAPIs:
    ins_namespace = Namespace('Vehicle APIs')

    ins_list_all_vehicles = ins_namespace.model('List of vehicles',{
        'str_source': fields.String(required=True, description='Source'),
        'str_destination': fields.String(required=True, description='Destination'),
    })

    ins_vehicle_detail = ins_namespace.model('Single Vehicle detail',{
        'str_vehicle_id': fields.String(required=True, description='Vehicle ID'),
    })

    