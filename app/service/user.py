from app import ins_db
from app.model import User

import random
import string

def login_user(request):
    dct_request = request.json
    try:
        ins_user = User.query.filter_by(
            vchr_username=dct_request.get("str_user_name"),
            vchr_password = dct_request.get("str_password")
        ).first()
        
        if ins_user:
            return {'status': 'success','message': 'Login success'}, 201    
        else:
            return {'status': 'fail','message': 'Invalid credentials'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 500

def signup_user(request):
    dct_request = request.json
    try:
        ins_user = User.query.filter_by(
            vchr_username=dct_request.get("str_user_name")
        ).first()
        
        if ins_user:
            return {'status': 'fail','message': 'Username already exists'}, 201    
        else:
            # create User
            ins_new_user = User(
                                pk_vchr_user_id = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 10)),
                                vchr_username=dct_request.get("str_user_name"),  
                                vchr_password=dct_request.get("str_password"))

            save_changes(ins_new_user)

            return {'status': 'success','message': 'User created successfully'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 500

def save_changes(data):
    ins_db.session.add(data)
    ins_db.session.commit()