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

    ins_add_new_vehicle = ins_namespace.model('New bus',{
        'vchr_org_username' : fields.String(required=True, description='Organization name'),
        'vchr_reg_no' : fields.String(required=True, description='Vehicle registration no'),
        'vchr_driver_name' : fields.String(required=False, description='Driver name'),
        'json_route_map': fields.String(required=True, description='Route'),
        'json_location': fields.String(required=True, description='Location coordinates'),
        'json_seat_map': fields.String(required=True, description='Seat map'),
        'vchr_name': fields.String(required=True, description='Name'),
        'int_direction': fields.Integer(required=True, description='Direction'),
        'int_dr_phone_no': fields.Integer(required=True, description='Phone Num')
    })

    