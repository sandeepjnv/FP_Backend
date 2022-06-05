from flask import request
from flask_restplus import Resource

# schema 
from app.schema import OrgAPIs
# service
from app.service import get_all_orgs , create_new_org, get_org_detail

ins_namespace = OrgAPIs.ins_namespace
ins_new_org = OrgAPIs.ins_add_new_org
ins_org_detail =OrgAPIs.ins_org_detail



@ins_namespace.route('/list_all_org')
class Users(Resource):
    @ins_namespace.doc("List all organizations")

    @ins_namespace.response(201, 'Fetched successfully')
    def get(self):
        """Get all ORG details""" 
        return get_all_orgs(request)

@ins_namespace.route('/get_organization_detail')
class Users(Resource):
    @ins_namespace.doc("Get org details")

    @ins_namespace.expect(ins_org_detail,validate = True)
    @ins_namespace.response(201, 'Fetched organization detail')
    @ins_namespace.doc('Input details')
    def post(self):
        """Fetch organization details""" 
        return get_org_detail(request)

@ins_namespace.route('/create_new_org')
class Users(Resource):
    @ins_namespace.doc("Create new organization")

    @ins_namespace.expect(ins_new_org,validate = True)
    @ins_namespace.response(201, 'Created new organization successfully!')
    @ins_namespace.doc('Input details')
    def post(self):
        """Create new organization account""" 
        return create_new_org(request)
        