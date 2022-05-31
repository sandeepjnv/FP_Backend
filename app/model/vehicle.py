from app import ins_db

class Vehicle(ins_db.Model):
    """ SeatMap Model for storing vehicle seat map related details """
    __tablename__ = "tbl_buses"

    pk_bint_vehicle_id = ins_db.Column(ins_db.BigInteger, primary_key=True, autoincrement=True)
    vchr_org_username = ins_db.Column(ins_db.String, nullable= False)
    vchr_reg_no = ins_db.Column(ins_db.String, nullable= False)
    vchr_driver_name = ins_db.Column(ins_db.String, nullable= False)
    vchr_status = ins_db.Column(ins_db.Boolean, nullable= False)
    json_route_map = ins_db.Column(ins_db.JSON, nullable=True)
    json_location = ins_db.Column(ins_db.JSON, nullable=True)
    json_seat_map = ins_db.Column(ins_db.JSON, nullable=True)
    vchr_name = ins_db.Column(ins_db.String, nullable= False)
    int_direction = ins_db.Column(ins_db.Integer ,nullable = False)
    
    def __repr__(self):
        return "<Seat map '{}'>".format(self.vchr_name)