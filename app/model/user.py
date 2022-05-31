from app import ins_db

class User(ins_db.Model):
    """ User Model for storing user related details """
    __tablename__ = "tbl_user"

    pk_vchr_user_id = ins_db.Column(ins_db.BigInteger, primary_key=True)
    vchr_username = ins_db.Column(ins_db.String, nullable=True)
    vchr_password = ins_db.Column(ins_db.String, nullable=False)
    
    def __repr__(self):
        return "<User '{}'>".format(self.vchr_username)