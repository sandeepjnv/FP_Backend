from app import ins_db
from app.model import Organization
import json
from datetime import datetime
import random,string

def get_all_orgs(request):
    try:
        ins_orgs = Organization.query.all()
        dct_orgs = {}
        for ins_org in ins_orgs:
            dct_org = ins_org.__dict__
            del dct_org["_sa_instance_state"]

            dct_orgs[dct_org["pk_vchr_org_id"]] = dct_org
        
        if dct_orgs:
            return dct_buses, 201    
        else:
            return {'status': 'fail','message': 'No Orgs found!'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 400

def create_new_org(request):
    dct_request = request.json
    try:
        ins_org = Organization(
            pk_vchr_org_id =  ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)),
            vchr_org_username = dct_request.get("vchr_org_username"),
            vchr_org_name = dct_request.get("vchr_org_name"),
            vchr_address = dct_request.get("vchr_address"),
            vchr_status = True,
            vchr_md_name = dct_request.get("vchr_md_name"),
            vchr_email = dct_request.get("vchr_email"),
            int_org_phone_no = dct_request.get("int_org_phone_no"),
            dat_created_date = datetime.now()
            )           
        ins_db.session.add(ins_org)
        ins_db.session.commit()

        return {'status': 'success','message': 'Organization added successfully'},201
    except Exception as e:
        print(e)
        return {'status': 'fail','message': 'Something went wrong'}, 400 

def get_org_detail(request):
    dct_request = request.json
    try:
        str_org_id = dct_request.get("str_org_id")

        ins_org = Organization.query.filter_by(pk_vchr_org_id=str_org_id).first()
        dct_org_detail = ins_org.__dict__
        del dct_org_detail["_sa_instance_state"]

        return dct_org_detail,201
    except Exception as e:
        print(e)
        return {'status': 'fail','message': 'Something went wrong'}, 400