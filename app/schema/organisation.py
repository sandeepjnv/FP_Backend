from flask_restplus import Namespace, fields

class OrgAPIs:
    ins_namespace = Namespace('Organization APIs')

    ins_org_detail = ins_namespace.model('Single Org detail',{
        'str_org_id': fields.String(required=True, description='Organization ID'),
    })

    ins_add_new_org = ins_namespace.model('New Organization',{
        'vchr_org_username' : fields.String(required=True, description='Organization username'),
        'vchr_org_name' : fields.String(required=True, description='Organization name'),
        'vchr_address' : fields.String(required=False, description='Organization address'),
        'vchr_email': fields.String(required=True, description='Email'),
        'vchr_md_name': fields.String(required=True, description='Director name'),
        'int_org_phone_no': fields.Integer(required=True, description='Phone Num')
    })

    