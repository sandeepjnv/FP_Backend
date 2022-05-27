from app import ins_db
from app.model import Buses
import json

def get_all_buses(request):
    dct_request = request.json
    try:
        ins_buses = Buses.query.all()
        dct_buses = {}
        for ins_bus in ins_buses:
            dct_bus = ins_bus.__dict__
            del dct_bus["_sa_instance_state"]

            # check for buses between routes

            dct_buses[ins_bus.pk_bint_vehicle_id] = dct_bus
        
        if dct_buses:
            return json.dumps(dct_buses), 201    
        else:
            return {'status': 'fail','message': 'No buses found with the corresponding ID'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 400

def get_bus_detail(request):
    dct_request = request.json
    try:
        str_bus_id = dt_request.get("str_vehicle_id")

        ins_bus = Buses.filter_by(pk_bint_vehicle_id=str_bus_id).first()
        print(ins_bus)
    except Exception as e:
        print(e)
        return {'status': 'fail','message': 'Something went wrong'}, 400 