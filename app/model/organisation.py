from app import ins_db

class Organization(ins_db.Model):
    """ Organization Model for storing organization related details """
    __tablename__ = "tbl_organization"

    pk_vchr_org_id = ins_db.Column(ins_db.String, primary_key=True)
    vchr_org_username = ins_db.Column(ins_db.String, nullable=True)
    vchr_org_name = ins_db.Column(ins_db.String, nullable=False)
    vchr_address = ins_db.Column(ins_db.String, nullable=False)
    vchr_md_name = ins_db.Column(ins_db.String, nullable=False)
    vchr_status = ins_db.Column(ins_db.Boolean, nullable=False)
    vchr_email = ins_db.Column(ins_db.String, nullable=False)
    int_org_phone_no = ins_db.Column(ins_db.Integer, nullable=False)
    dat_created_date = ins_db.Column(ins_db.String, nullable=False)
    
    def __repr__(self):
        return "<User '{}'>".format(self.vchr_username)