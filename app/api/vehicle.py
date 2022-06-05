from flask import request
from flask_restplus import Resource

# schema 
from app.schema import VehicleAPIs
# service
from app.service import get_all_buses , get_bus_detail ,add_new_bus

ins_namespace = VehicleAPIs.ins_namespace
ins_list_all_vehicles = VehicleAPIs.ins_list_all_vehicles
ins_vehicle_detail = VehicleAPIs.ins_vehicle_detail
ins_new_bus = VehicleAPIs.ins_add_new_vehicle

@ins_namespace.route('/list_all_vehicles')
class ListAllVehicles(Resource):
    @ins_namespace.doc("List all vehicles")

    @ins_namespace.expect(ins_list_all_vehicles,validate = True)
    @ins_namespace.response(201, 'List of all vehicles retrieved')
    @ins_namespace.doc('Input source and destination')
    def post(self):
        """List all vehicles""" 
        return get_all_buses(request)

@ins_namespace.route('/get_bus_detail')
class BusDetail(Resource):
    @ins_namespace.doc("Get a vehicle detail")

    @ins_namespace.expect(ins_vehicle_detail,validate = True)
    @ins_namespace.response(201, 'Detail of a vehicle retrieved')
    @ins_namespace.doc('Input vehicle ID')
    def post(self):
        """Get a vehicle detail""" 
        return get_bus_detail(request)

@ins_namespace.route('/add_new_bus')
class BusDetail(Resource):
    @ins_namespace.doc("Add new bus")

    @ins_namespace.expect(ins_new_bus,validate = True)
    @ins_namespace.response(201, 'New bus detailed')
    @ins_namespace.doc('Input vehicle details')
    def post(self):
        """Add new vehicle """ 
        return add_new_bus(request)