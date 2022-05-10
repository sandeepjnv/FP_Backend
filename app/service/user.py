from app import ins_db
from app.model import User

def user_login(request):
    dct_request = request.json()
    try:
        ins_user = User.query.filter_by(
            vchr_username=request.get("str_username"),
            vchr_password = request
        ).first().get()  
        
        if ins_user:
            return {'status': 'success','message': 'Login success'}, 201    
        else:
            return {'status': 'fail','message': 'Login failed'}, 201    
        
    except Exception as msg:
        print(str(msg))
        return {'status': 'fail','message': str(msg),}, 500