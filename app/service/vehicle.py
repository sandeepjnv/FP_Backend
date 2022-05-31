from app import ins_db
from app.model import Vehicle
import json

def get_all_buses(request):
    dct_request = request.json
    source_lat , source_long = dct_request.get("str_source").split(",")
    dest_lat , dest_long = dct_request.get("str_destination").split(",")
    try:
        ins_buses = Vehicle.query.all()
        dct_buses = {}
        for ins_bus in ins_buses:
            dct_bus = ins_bus.__dict__
            del dct_bus["_sa_instance_state"]

            # check for buses between routes
            intDirection = dct_bus["int_direction"]
            if int_direction == 0:
                arrRoute = dct_bus["json_route_map"].reverse()
            else:
                arrRoute = dct_bus["json_route_map"]

            blnSource = False
            blnDestination = False
            for stop in arrRoute:
                if blnSource and blnDestination:
                    # stop looping stops ,skip current bus and check next bus                    
                    break
                else:
                    stop_lat,stop_long = stop.split(",")

                    if not blnSource:
                        if source_lat == stop_lat and source_long == stop_long:
                            # source matched look for dest
                            blnSource = True
                    else:
                        if dest_lat == stop_lat and dest_long == stop_long:
                            blnDestination = True
                            dct_buses[ins_bus.pk_bint_vehicle_id] = dct_bus
        
        if dct_buses:
            return dct_buses, 201    
        else:
            return {'status': 'fail','message': 'No buses found with the corresponding ID'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 400

def get_bus_detail(request):
    dct_request = request.json
    try:
        str_bus_id = dct_request.get("str_vehicle_id")

        ins_bus = Vehicle.query.filter_by(pk_bint_vehicle_id=str_bus_id).first()
        dct_bus_detail = ins_bus.__dict__
        del dct_bus_detail["_sa_instance_state"]

        return dct_bus_detail,201
    except Exception as e:
        print(e)
        return {'status': 'fail','message': 'Something went wrong'}, 400 