from functools import wraps
from flask import request, jsonify


class UserAuthenticator:
    def __init__(self, auth_service):
        self.auth_service = auth_service
    
    def authenticate(self, auth_header):
        try:
            return self.auth_service.login(auth_header)
        except Exception:
            return None
    
    def require_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            user_id = self.authenticate(auth_header)
            if user_id is None:
                return jsonify({'error': 'Unauthorized'}), 401
            request.current_user_id = user_id
            return f(*args, **kwargs)
        return decorated