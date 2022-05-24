from app import ins_db

class SeatMap(ins_db.Model):
    """ SeatMap Model for storing vehicle seat map related details """
    __tablename__ = "tbl_seat_map"

    pk_bint_vechicle_id = ins_db.Column(ins_db.BigInteger, primary_key=True, autoincrement=True)
    json_seat_map = ins_db.Column(ins_db.JSON, nullable=True)
    
    def __repr__(self):
        return "<Seat map '{}'>".format(self.pk_bint_vechicle_id)